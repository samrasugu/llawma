from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl

DB_FAISS_PATH = "vectorstore/db_faiss"

custom_prompt_template = """
Use the following pieces of information to answer the user's questions. 
If you don't know the answer, please just say that you do not know it, don't try to make up an answer.

Context: {context}
Question: {question}
Only return the helpful answer below and nothing else.


""" #Mitigate model hallucination


def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vector stores.
    """

    prompt = PromptTemplate(template=custom_prompt_template, input_variables=[
                            'context', 'question', ])

    return prompt


def load_llm():
    """
    Load the LLM model.
    """

    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5,
    )
    return llm


def retrieval_qa_chain(llm, prompt, db):
    """
    Create a retrieval QA chain.
    """

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(
            search_kwargs={"k": 2},
        ),
        return_source_documents=True,
        chain_type_kwargs={
            "prompt": prompt,
        }
    )
    return qa_chain


def qa_bot():
    """
    Define a QA bot.
    """

    embeddings = HuggingFaceEmbeddings(
        # TODO: Change the device to GPU if you have one
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

    vector_db = FAISS.load_local(DB_FAISS_PATH, embeddings)

    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, vector_db)

    return qa


def final_result(query):
    qa_result = qa_bot()
    response = qa_result({"query": query})
    return response

# CHAINLIT


@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting Llawma...")

    await msg.send()
    msg.content = "Hi, Welcome to the Llawma chatbot. I am here to help you win cases. Please ask me a question."

    await msg.update()
    cl.user_session.set("chain", chain)


@cl.on_message
async def main(message: cl.Message):
    # chain = cl.user_session.get("chain")
    # chain = cl.user_session.set("chain")
    chain = cl.user_session.get("chain")
    # callback = cl.AsyncLangchainCallbackHandler(
    #     stream_final_answer=True,
    #     answer_prefix_tokens=["FINAL", "ANSWER"],)
    # callback.answer_reached = True
    callback = cl.AsyncLangchainCallbackHandler()
    res = await chain.acall(message.content, callbacks=[callback])
    
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        answer += f"\nSources:\n" + str(sources)
    else:
        answer += f"\nNo sources found."
    
    await cl.Message(content=answer).send()


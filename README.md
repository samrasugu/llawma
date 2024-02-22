# Llawma Bot

The Llawma Bot is a powerful tool designed to junior associates prepare for court cases through the ingestion of context on the case and the subsequent generation of in-court arguments, opening and closing statements. This README will guide you through the setup and usage of the bot.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can start using the Llawma Bot, make sure you have the following prerequisites installed on your system:

- Python 3.6 or higher
- Required Python packages (you can install them using pip):
  - langchain
  - chainlit
  - sentence-transformers
  - faiss
  - PyPDF2 (for PDF document loading)

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/barrywire/llawma.git
   cd llawma
   ```

2. Create a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the required large language model and data. Please refer to the Langchain documentation for specific instructions on how to download and set up the language model and vector store. In this case, the LLM is found here: [The Bloke - HuggingFace](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin)

5. Set up the necessary paths and configurations in your project, including the `DB_FAISS_PATH` variable and other configurations as per your needs.

## Getting Started

To get started with the Llawma Bot, you need to:

1. Set up your environment and install the required packages as described in the Installation section.

2. Configure your project by updating the `DB_FAISS_PATH` variable and any other custom configurations in the code.

3. In your terminal, run the following command to initiate the ingestion engine:

   ```bash
   python ingest.py
   ```

4. In your terminal, run the following command to initiate the chatbot:

   ```bash
   chainlit run model.py -w
   ```

## Usage

The Llawma Bot can be used for answering law-related queries. To use the bot, you can follow these steps:

1. Start the bot by running your application or using the provided Python script.

2. Send a law-related query to the bot.

3. The bot will provide a response based on the information available in its database.

4. If sources are found, they will be provided alongside the answer.

5. The bot can be customized to return specific information based on the query and context provided.

## Contributing

Contributions to the Llawma Bot are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Create a new branch for your feature or bug fix.

3. Make your changes and ensure that the code passes all tests.

4. Create a pull request to the main repository, explaining your changes and improvements.

5. Your pull request will be reviewed, and if approved, it will be merged into the main codebase.

## License

This project is licensed under the MIT License.

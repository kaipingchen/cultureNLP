# Applications for Human-Chatbot Conversations on Contentious Topics 

This project builds upon the [chat-with-gpt-3](https://github.com/Top34051/chat-with-gpt-3) codebase, with modifications to better align with its research objectives. These include replacing the base model with Llama-3.1-70B-Instruct, restricting the chatbot’s conversations to specific topics, introducing the option for it to act as a cultural representative (or encouraging it to remain neutral), and implementing a feedback page following the conversation.

In this study, the chatbot engages with American and Latinx participants on controversial topics—abortion, the death penalty, GMOs, and LGBTQ rights—in English, Spanish, or Portuguese, depending on the participant's native language. The chatbot either assumes the role of a cultural deliberator from a Western (U.S.) or Latinx (Brazil, Colombia, Mexico, or Nicaragua) perspective, engaging in deliberative communication, or, when encouraged to remain neutral, exhibits a more stubborn conversational style with the intention of not representing any specific cultural values.

## Overview

These applications were developed using Python and rely on [Streamlit](https://www.streamlit.io/), a framework designed for creating ML and data science applications. We utilize [MongoDB](https://www.mongodb.com/) as the storage solution for the conversations and deploy the application on Streamlit's [sharing platform](https://share.streamlit.io/). This repository provides the application's source code, along with instructions for setup and deployment.

## Setup

### Clone the repository

To begin, clone the repository by running the following command:

```bash
git clone https://github.com/kaipingchen/cultureNLP.git
```

### Install dependencies

Create a virtual environment by running ```python -m venv venv```. Activate it using ```source venv/bin/activate``` (macOS/Linux) or ```.\venv\Scripts\activate``` (Windows). Run ```deactivate``` to exit.

In the activated virtual environment, install Python 3.13.0. Then install the required dependencies by executing the following command:

```bash
pip install -r requirements.txt
```

### MongoDB Setup

The application relies on MongoDB for storing conversations. To set up MongoDB, please follow the instructions [here](https://docs.mongodb.com/manual/installation/). Once MongoDB is set up, proceed with their guidelines to create a database. As specified in `utils.database.py`, the name of the database and collection for this project are `latinx-nlp` and `user-data`, respectively. Either create a database and collection with the same names, or specify different names and ensure that they are changed accordingly in `utils.database.py`. Afterward, create a directory `.streamlit` and add your MongoDB connection string to the `.streamlit/secrets.toml` file.

### DeepInfra API Setup for LLaMA Access

To enable response generation using the DeepInfra API, you need to set up the API. Refer to the instructions [here](https://deepinfra.com/docs/deep_infra_api) for the necessary steps. Place your API key in the `secrets.toml` file. Once both MongoDB and the DeepInfra API are properly configured, your `secrets.toml` file should resemble the following:

```toml
llama_api_key = <YOUR DEEPINFRA API KEY>
mongo_uri = <YOUR MONGODB CONNECTION STRING>
```

## Deployment

In the context of this project, these apps were accessed via a link provided in a pre-survey. The pre-survey generated an ID that was then concatenated to the deployed app link as a query parameter, which was the user's unique ID that was entered into the database for post-chat analysis. Without the query parameter `/?id=<ID>` at the end of the app link, whether local or deployed, all submissions to the database will have the same ID, which will not allow for unique identification.

If you intend to use this code on a large scale for research purposes, ensure the addition of an ID query parameter to change the code to suit your needs.

### Local deployment

To run the application locally, execute `streamlit run <APP_NAME>.py` on any of the 56 available apps. For instance:

```bash
streamlit run latino_delib-EN-abortion-brazil.py
streamlit run no_delib-ES-deathpenalty.py
streamlit run western_delib-PR-lgbt-US.py
```

Each command corresponds to a different app. The first command launches the deliberative, representative-of-Brazilian-culture chatbot whose focus is on abortion in English. The second launches the non-deliberative, no culture chatbot whose focus is on the death penalty in Spanish, while the third launches the deliberative, representative-of-American-culture chatbot whose focus is on LGBTQ rights in Portuguese.

### Streamlit sharing deployment

To deploy the application on Streamlit sharing, follow the instructions [here](https://docs.streamlit.io/en/stable/deploy_streamlit_app.html). Make sure to add your MongoDB connection string and DeepInfra API key to the `secrets.toml` file. Once the application is deployed, you can access it through the link provided by Streamlit sharing.

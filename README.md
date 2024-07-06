# RAG Mini Bootcamp
In this pilot course, you'll build a Naive RAG-based question-answer agent that supports the following HTML documents:
- [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/html/2312.10997v5)
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)  

Understanding Naive RAG architecture is the first step towards understanding more advanced architectures and techniques appropriate for production settings.

# Repo Structure
```
.
├── .devcontainer  # Docker environment config files
├── 1 query_qa_rag_agent.ipynb  # Start here. Use to check your environment works.
├── 2 indexer.ipynb  # Tutorial 2
├── 3 retriever.ipynb  # Tutorial 3
├── 4 generator.ipynb  # Tutorial 4
├── 5 summary.ipynb  # Tutorial 5
├── LICENSE
├── README.md
├── cheat_code  # Completed, working code you can cheat off of if you get stuck
├── data  # Nothing useful in here for now
├── requirements.txt  # Python packages
└── workshop_code  # The code you will edit in the tutorials
```

# Dev Machine Setup

## Install Docker
Your development environment will be in a VSCode Dev Container to eliminate "works on my machine" issues. Due to variability in how individual developers configure their base OS, around 50% of course attendees have environment-related issues completing the tutorial if using their base OS instead of a container.

On a clean OS configuration, Python venv will also work. If you are familiar with using venv and are confident your OS doesn't have a conflicting environment manager like conda persistent, you may use venv instead.

Recent OS distributions no longer support system-level installation of Python packages.

If you want to push your changes to your own fork, note that your SSH settings won't be copied to your Dev Container. So, you'll need to push your changes from outside the container on your local machine. Technically, SSH can be configured, but I didn't have time to figure out how to make SSH on Dev Container automatically work on both Windows and Mac.

If you want to inspect the environment configuration, check out the folder ".devcontainer/". Feel free to ask any questions.

## Install VSCode
We will use VSCode for this tutorial because it supports both Python Notebooks and standard Python editing. Although other editors have their merits, VSCode is also the most standard editor in 2024. The containerized development environment is only tested to work with VSCode. You must use VSCode to get instructor or TA support during the workshop. 

## Install VSCode Remote Containers Extension
You will use this extension to develop within the Docker container dev environment.

Open VSCode > Extensions. Search for "Remote Containers". Click install.

## Install Git (Mac & *Nix)
If you're not sure, check if you have `git` installed already. Copy and paste this commmand into your terminal:
```
if command -v git &>/dev/null; then echo "Git is installed and on the PATH"; else echo "Git is not installed or not on the PATH"; fi
```

If it's not installed, install git using Homebrew, Apt, etc as appropriate.

## Install Git (Windows)
Easy option: install Git Bash  

Microsoft Official Option:
1. Install Windows Subsystem for Linux
2. Open Ubuntu shell
3. `apt install git`

<!-- ## Install Python
Check for a working Python installation by launching a terminal and run the following command:  
```
python3 --version
```

It should display the Python version you have installed. -->

# Repo Setup

## Fork and Clone the Repo
1. Go to [the Github repo for this course](https://github.com/tobkin/rag-mini-bootcamp)
2. Click Fork
3. Clone your forked repo with a terminal
4. `cd` into the `rag-mini-bootcamp` repo folder

<!-- ## Create Virtual Environment & Install Dependencies
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
``` -->

## .env File Setup
We will use OpenAI embeddings, GPT3.5, and Pinecone vector database for this tutorial, so you will need to securely store your API keys in a `.env` file. This file is in `.gitignore` so it doesn't accidentally get committed to the repo where your keys would be exposed.  

Create a `.env` file in the root of the repo from this template:  
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## OpenAI API Setup
Go to OpenAI API settings. Create a new API key and copy it to the `.env` file. If you're out of free trial credits, purchase $5 of credits.

## Pinecone VectorDB Setup
Create a Pinecone account. Create a new index.
- Index Name: "textsplits"
- Configuration: Setup by model > text-embedding-3-small
- Capacity Mode: serverless
- Cloud Provider: doesn't matter
- Region: default
- Click "Create Index"

# Test Your Environment  
Open the folder "rag-mini-bootcamp" in VSCode. Open the folder in Dev Container mode by using Cmd/Ctrl + Shift + P > Dev Containers: Open Folder in Container. The first time, the container will take some time to build while it downloads the required packages.

Once the container is finished building, open `./query_qa_rag_agent.ipynb` in VSCode. Click "Run All". The notebook should display a GPT3.5 completion to the question about the paper. If you get an error, try to diagnose it or flag one of us for help.

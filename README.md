# AI_Agent Project
Multiple LLM Based AI Agent work together to gather information about stocks, to process financial details and market sentiments and to advice to perform trade.

## Dependencies for the project

1. Python version==3.10.0
2. Anaconda setup
3. API key from https://serper.dev/login
4. API key from https://console.groq.com/keys
5. API key from https://account.browserless.io/
6. API key from https://sec-api.io/login

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/AnuragRaut08/AI-Agent.git
```

move to other folder

```bash
mv ././AI-Agent AI folder
```


### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n AI folder python=3.10 -y
```

### STEP 02- install all the dependencis
```bash
poetry install --no-root
```



### STEP 03- SET API Keys in env file 

```bash
#set api keys in .env file
#ie: BROWSERLESS_API_KEY=756209
```

```bash
# Finally run the following
python app.py
```


```bash
Author: Anurag Raut
Anurag Raut
Email: anuragtraut2003@gmail.com

```

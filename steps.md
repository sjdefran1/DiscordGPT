### @Author: Sam DeFrancisco [LinkedIn](https://www.linkedin.com/in/sam-defrancisco-4373361b3/)

---

# Creating a Discord ChatGPT Bot Using Python

## Prerequistes For Entire Project

- Working Python Installation on your device
- PIP (python package manager)
  - Knowledge of python as well as PIP

> Throughout this tutorial I will be assuming the reader knows how to setup there own development enviroment. If the reader needs assistance installing python/pip they sould **refer to links below.**

[Python Windows Install](https://www.digitalocean.com/community/tutorials/install-python-windows-10) | [Python Mac Install](https://www.dataquest.io/blog/installing-python-on-mac/) | [Python Linux Install](https://docs.python-guide.org/starting/install3/linux/)

[PIP Windows Install](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) | [PIP Mac Install](https://www.geeksforgeeks.org/how-to-install-pip-in-macos/) | [PIP Linux Install](https://www.tecmint.com/install-pip-in-linux/)

---

# Setting up ChatGPT

## Prereqs

- OpenAI account

## Generate an API Key

To be able to connect to ChatGPT using Python we will need an API key, this will uniquely identify our OpenAI account to the code we are writing.

**continued on next page**
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## First navigate to [OpenAi Homepage](https://platform.openai.com/overview)

![](ss/openAiAcct.png)

- In the top right of the screen click login and enter your credentials
  > You may have to verify that you are a human
- Once logged in, click on your account once again in the top right

  - From the dropdown, choose **View API Keys**
  - In the middle of your screen click **Create New Secret Key**

    > **This key will only be displayed once!** It is important that you save it somewhere right away before clicking out of the popup

    If something goes wrong you can always create a new API key

### <span style="color: #fc727b">It is very important that you never share your API key w/ anyone else!</span>

---

## Lets Make Sure Our Key is Working!

- First lets install the necessary packages to test out our key
  - Within your **console** enter the following pip installs
    ```bash
    pip install openai
    ```
    ```bash
    pip install python-dotenv
    ```
- Now create a file called .env wherever you want this project to live, I reccomend creating a folder to hold these files, call it whatever you like for example DiscordOpenAI
  - Inside .env add your api key as follows
    ```
    OPENAI_API_KEY={Your api key}
    ```
    > Make sure to replace {your api key} with the key we just generated, **do not include the brackets**
- Create a new python file called test.py & import the necessary packages by adding the following lines
  ```python
  import os
  import openai
  from dotenv import load_dotenv
  ```
- Next we are going to load our .env file into our python file using dotenv
  ```python
  load_dotenv()
  ```

### Now the fun part, lets connect to chatGPT and generate our first response.

```python
# Load in our API key, because of dotenv we don't have to mess with our actual
# System variables, it loads them in itself
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a string that holds our prompt
# The prompt can be whatever you'd like
gpt_prompt = "Say hello five different ways"

# Now for the actual query
# While this might look a little overwhelming it isn't anything to bad
# The two most import parts here are our engine & prompt
# engine: refers to the data model we are accessing
# prompt: our prompt string, what we are asking GPT
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=gpt_prompt,
  temperature=0.5,
  max_tokens=256,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

# print the response from GPT to the console
# response has a lot of extra information included in it, to access just the response
# we index it in this way
print(response['choices'][0]['text'])
```

---

### If all goes well here we should get our response printed to the console, heres mine!

```
Hello,

Hi,

Hey,

What's up,

Yo.
```

---

# Discord

> [Discord Developer Getting Started Guide](https://discord.com/developers/docs/getting-started), information below could become deprecated, this link should always have the most up-to-date information

## Prereqs

- Discord Account

## Steps

1. Create discord server
2. Open discord developer dashboard
3. Create Application
4. Create Bot
5. Generate Bot url link
   1. Paste link into browser to activate

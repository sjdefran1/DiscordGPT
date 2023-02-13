### @Author: Sam DeFrancisco

---

# Create Discord ChatGPT Bot Using Python

## Prerequistes For Entire Project

- Working Python Installation on your device
- PIP (python package manager)
  - Knowledge of python as well as PIP

> Throughout this tutorial I will be assuming the reader knows how to setup there own development enviroment. If the reader needs assistance installing python or pip they sould refer to links below.

- Python Windows Install | Python Mac Install | Python Linux Install
- PIP Windows Install | PIP Mac Install | PIP Linux Install

---

# ChatGPT

## Prereqs

- OpenAI account

## Generate an API Key

To be able to connect to ChatGPT using Python we will need an API key, this will uniquely identify our OpenAI account to the code we are writing.

## First navigate to https://platform.openai.com/overview

- In the top right of the screen click `login` and enter your credentials
  > You may have to verify that you are a human
- Once Logged in click on your account once again in the top right

  - Choose **`View API Keys`**
  - In the middle of your screen click **`Create New Secret Key`**

    > **This key will only be displayed once!** It is important that you save it somewhere right away before clicking out of the popup

    If something goes wrong you can always create a new API key

### <span style="color: #fc727b">It is very important that you never share your API key w/ anyone else!</span>

---

## Lets Make Sure Our Key is Working!

# Discord

> Getting started guide https://discord.com/developers/docs/getting-started

## Prereqs

- Discord Account

## Steps

1. Create discord server
2. Open discord developer dashboard
3. Create Application
4. Create Bot
5. Generate Bot url link
   1. Paste link into browser to activate

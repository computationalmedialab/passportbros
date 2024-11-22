# Passport Bros Reddit Analysis Project

## Project Overview

This project focuses on analyzing Reddit posts from six subreddit forums within the Passport Bros community. Using Python, natural language processing (NLP), and a custom large-language model (LLM) built on ChatGPT, we explored themes, patterns, and the unique characteristics of discussions within these forums. The ultimate goal was to differentiate between the subreddits and categorize their content into meaningful clusters.

---

## Materials and Methods

### Data Collection

- **Tool Used:** Python Reddit API Wrapper (PRAW)
- **Subreddits Analyzed:**
  - r/Passport_Bros
  - r/passportbro
  - r/PassportBrosHQ
  - r/PassportBrosOnTop
  - r/passportbrosunited
  - r/ThePassportBros
- **Collection Process:**
  - Up to 3,500 posts were scraped per subreddit using keywords related to "Passport Bros."
  - Metrics collected included:
    - Subreddit name
    - Post title
    - Date of post
    - Number of comments
    - Number of upvotes
    - Post URL
  - Data was segmented into six datasets based on subreddit names.

### Data Analysis

- **Custom GPT Model:** A specialized GPT, named **PassportBrosGPT**, was developed using ChatGPT-4.0. 
  - **Features:**
    - Instruction set to avoid hallucination and misinformation.
    - Knowledge base including Passport Bros terminology and themes.
  - **Prompts Used:**
    - **Theme Assignment:** Identify themes for each post using NLP and categorize into a table with two columns: "Reddit Posts" and "Themes."
    - **Summary Creation:** Summarize themes for each subreddit dataset.
    - **Clustering:** Differentiate themes across datasets and generate six thematic clusters.

- **Repetition and Testing:**
  - The analysis was repeated across five separate conversations to observe variations in output and refine insights.

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

## Results

### Differentiators

Key distinctions among subreddits emerged from the analysis:
- **r/Passport_Bros and r/PassportBrosHQ:** Discussions on sex tourism and international dating, with a focus on Colombia.
- **r/passportbro and r/passportbrosunited:** General travel inquiries with limited focus on social experiences.
- **r/ThePassportBros:** Predominantly social experiences and dating discussions.

### Clustering

Six thematic clusters were developed:
1. **Practical Travel:** Focus on logistics and advice-sharing (e.g., r/passportbro, r/passportbrosunited).
2. **Travel & Social Balance:** Blend of travel advice and dating/social experiences (e.g., r/PassportBrosHQ, r/PassportBrosOnTop).
3. **Social Experiences:** Interactions with women abroad alongside some travel advice (e.g., r/Passport_Bros, r/ThePassportBros).
4. **Regional Focus:** Discussions on travel and dating in specific countries/regions (e.g., r/Passport_Bros, r/ThePassportBros).
5. **Movement Ethos:** Exploration of motivations and ideologies behind Passport Bros (e.g., r/PassportBrosOnTop, r/PassportBrosHQ).
6. **Niche Topics:** Unique discussions on cryptocurrency, economics, and cultural insights (e.g., r/passportbrosunited).

### Insights

- While united by a shared interest in international travel, subreddits cater to diverse aspects of the Passport Bros movement, ranging from logistics and dating to movement ideology and niche topics.
- The clusters reflect a variety of interests but often converge on the common goal of seeking relationships abroad.

---

## Contact Information

For any questions or further information about this project, please reach out to the project contributors.

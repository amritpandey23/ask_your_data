# Insights generation tool using GenAI

> Caution: This is a hobby project! The code is poorly rewritten.

Powered by Google's Gemini 1.5 Flash.

## What?

Insight generation tool helps you to generate insights/ draw graphs and charts on the CSV file provided by you.

## Screenshots

![](./static/home_page.png)
![](./static/results.png)

## Setup

1. Get a Google AI account with access to Gemini from Google AI Studio. Populate the `.env.example` file the Gemini API Key and rename it `.env`.
2. Create virtual environment and install dependencies.
3. Run project with `python web.py`.
4. (Optional) If you want command line script then run `python app.py` after filling the `DATA_PATH` and `questions` variables in `app.py`.

## Working

![](./static/working.png)

## License

MIT

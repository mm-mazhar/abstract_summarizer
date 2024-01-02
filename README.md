# Abstract Summarizer

The Abstract Summarizer project utilizes the power of the google/pegasus-xsum model from the Hugging Face Transformers library to provide an easy-to-use interface for summarizing text. This Streamlit app allows users to input text and receive concise summaries based on various parameters. Model tries to use new words during summarization process.

## Features

- User-Friendly Interface: The Streamlit app provides a simple and intuitive user interface, making it easy for users to interact with the abstract summarization tool.

- Customizable Summarization: Users can customize the summarization process by adjusting parameters such as max length, min length, length penalty, number of beams, and early stopping. This flexibility ensures that users can fine-tune the summarization output according to their preferences.

- Efficient Summarization: Leveraging the google/pegasus-xsum model, the app generates accurate and coherent summaries of input text. The summarizer function handles tokenization, model inference, and text cleanup to deliver high-quality results.

- Responsive Design: The Streamlit app incorporates a responsive design, allowing users to seamlessly interact with the tool on various devices.

## How to Use

- Play areound with the following input parameters. Usually works best with the low values in max length, min length.

- Input Parameters: Adjust parameters such as max length, min length, length penalty, number of beams, and enable or disable early stopping through the sidebar.

- Enter Text: Input the text you want to summarize into the provided text area.

- Summarize: Click the "Summarize" button to initiate the summarization process.

- View Summary: The app displays the generated summary, providing users with a concise version of the input text.

## Requirements

The project relies on the following Python packages, which can be installed using the provided requirements.txt file:

transformers: Provides access to transformer models, including Pegasus.
streamlit: Enables the creation of interactive web applications.
Other dependencies required for the project's functionality.
How to Run:

- Clone the repository: git clone `https://github.com/mm-mazhar/abstract_summarizer.git`
- Navigate to the project directory: cd abstract_summarizer
- Install dependencies: `pip install -r requirements.txt`
- Run the Streamlit app: `streamlit run app.py`

Note: Ensure that you have Python and pip installed on your system.

### Contributions

Contributions to enhance the functionality, UI/UX, or add new features are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

### License

This project is open-source and available under the <b>MIT License</b>

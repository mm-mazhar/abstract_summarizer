import streamlit as st

from abstract_summarizer import abstract_summarizer

# st.set_page_config(layout = "wide")
st.set_page_config(page_title="Abstract Summarizer", page_icon="🤖")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 340px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 340px;
        margin-left: -340px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h3 style='text-align: center; color: Black; font-family: font of choice, fallback font no1, sans-serif;'>Abstract Summarizer</h3>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: red; font-family: font of choice, fallback font no1, sans-serif;'>Summarize your text with google/pegasus-xsum</h4>",
    unsafe_allow_html=True,
)
st.markdown("#")


def main():
    # st.title("Abstract Summarizer")
    # st.subheader("Summarize your text with google/pegasus-xsum")

    # Sidebar input parameters
    max_length = st.sidebar.slider(
        "Max Length", min_value=50, max_value=2048, value=1024
    )
    min_length = st.sidebar.slider("Min Length", min_value=10, max_value=400, value=50)
    length_penalty = st.sidebar.slider(
        "Length Penalty", min_value=0.1, max_value=5.0, value=2.0
    )
    num_beams = st.sidebar.slider("Number of Beams", min_value=1, max_value=10, value=4)
    early_stopping = st.sidebar.checkbox("Early Stopping", value=True)

    # Get user input
    user_input = st.text_area("Enter text to summarize:")

    if st.button("Summarize"):
        if user_input:
            # Call the summarizer function with sidebar parameters
            summary = abstract_summarizer(
                user_input,
                max_length,
                min_length,
                length_penalty,
                num_beams,
                early_stopping,
            )

            # Display the summary
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")


if __name__ == "__main__":
    main()

from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import re

# LOAD TOKENIZER
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
# LOAD MODEL
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")



def abstract_summarizer(
    input_text, max_length, min_length, length_penalty, num_beams, early_stopping
):
    # CREATE TOKENS | NUMBER REPRESENTATION OF TEXT
    tokens = tokenizer(
        input_text, truncation=True, padding="longest", return_tensors="pt"
    )

    # SUMMARIZE
    summary = model.generate(
        **tokens,
        max_length=max_length,
        min_length=min_length,
        length_penalty=length_penalty,
        num_beams=num_beams,
        early_stopping=early_stopping,
    )

    # DECODE/CONVERT SUMMARY TOKENS TO TEXT
    decoded_summary = tokenizer.decode(summary[0], clean_up_tokenization_spaces=True)

    # TEXT CLEANUP
    decoded_summary = decoded_summary.replace("[CLS]", "").replace("[SEP]", "")
    decoded_summary = decoded_summary.replace("<pad>", "").replace("</s>", "")
    decoded_summary = re.sub(r"\[\d+\]", "", decoded_summary)

    return decoded_summary
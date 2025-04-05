from langchain.text_splitter import CharacterTextSplitter

text = """With the online text generator you can process your personal Lorem Ipsum enriching it with html elements that define its structure, with the possibility to insert external links, but not only.

Now to compose a text Lorem Ipsum is much more fun!

In fact, inserting any fantasy text or a famous text, be it a poem, a speech, a literary passage, a song's text, etc., our text generator will provide the random extraction of terms and steps to compose your own exclusive Lorem Ipsum.

Be original, test your imagination... our Lorem Ipsum generator will amaze you. Try it now! Copy and Paste!
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

chunks = splitter.split_text(text)

print(chunks)
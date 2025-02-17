from mentat.config import Config

title = "Pre tags around mentat output"

description = """
We changed the conversation viewer to use pre tags to display whitespace as it is outputed.
We had to set line wrap so users wouldn't have to side scroll.
"""

prompts = [
    "Change the conversation viewer to display whitespace in the messages unchanged.",
    (
        "Change the conversation viewer to display whitespace in the messages"
        " unchanged. Be sure the lines still wrap so side scrolling isn't necessary."
    ),
    (
        "Remove the logic from the conversatin viewer that replaces new lines with"
        " breaks and add pre tags. Set it to pre-wrap with css so side scrolling isn't"
        " necessary."
    ),
]

repo = "https://github.com/AbanteAI/mentat"
commit = "b8d90b89e4a0d7ad266bf914c4ce99c473dd8dc0"

config = Config(
    auto_context=True,
    maximum_context=8000,
)

comparison_commit = "1f21444d9b35caa0a576ad02c38a1f58350afb27"

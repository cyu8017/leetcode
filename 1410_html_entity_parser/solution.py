class Solution:
    def entityParser(self, text):
        entities = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">",
                    "&lt;": "<", "&frasl;": "/"}
        for encoded, decoded in entities.items():
            text = text.replace(encoded, decoded)
        return text

// LeetCode 1410: Html Entity Parser

function entityParser(text: any): any {
    const entities = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"};
    return text.replace(/&quot;|&apos;|&amp;|&gt;|&lt;|&frasl;/g: any, (match: any): any => entities[match]);
}

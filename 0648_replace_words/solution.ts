// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

export function replaceWords(dictionary: string[], sentence: string): string {
    const roots = new Set(dictionary);
    const words = sentence.split(" ");
    const result = [];
    for (const word of words) {
        let replacement = word;
        for (let i = 1; i <= word.length; ++i) {
            const prefix = word.substring(0, i);
            if (roots.has(prefix)) {
                replacement = prefix;
                break;
            }
        }
        result.push(replacement);
    }
    return result.join(" ");
}

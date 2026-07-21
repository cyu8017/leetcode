// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

function longestWord(words: string[]): string {
    const wordSet = new Set(words);
    let best = "";
    for (const word of words) {
        let prefix = word;
        let valid = true;
        while (prefix) {
            if (!wordSet.has(prefix)) {
                valid = false;
                break;
            }
            prefix = prefix.slice(0, -1);
        }
        if (valid && (word.length > best.length || (word.length === best.length && word < best))) {
            best = word;
        }
    }
    return best;
}

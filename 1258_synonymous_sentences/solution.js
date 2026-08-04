// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

/**
 * @param {string[][]} synonyms
 * @param {string} text
 * @return {string[]}
 */
var generateSentences = function(synonyms, text) {
    const parent = new Map();
    const find = (x) => {
        if (!parent.has(x)) parent.set(x, x);
        if (parent.get(x) !== x) parent.set(x, find(parent.get(x)));
        return parent.get(x);
    };
    for (const [a, b] of synonyms) {
        const ra = find(a), rb = find(b);
        parent.set(ra, rb);
    }
    const groups = new Map();
    for (const word of parent.keys()) {
        const root = find(word);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root).push(word);
    }
    for (const list of groups.values()) list.sort();
    const words = text.split(" ");
    const choices = words.map((w) => (parent.has(w) ? groups.get(find(w)) : [w]));
    const answer = [];
    const build = (i, parts) => {
        if (i === choices.length) {
            answer.push(parts.join(" "));
            return;
        }
        for (const word of choices[i]) {
            parts.push(word);
            build(i + 1, parts);
            parts.pop();
        }
    };
    build(0, []);
    return answer;
};

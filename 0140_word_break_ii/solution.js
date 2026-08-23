// LeetCode 0140 - Word Break II
// https://leetcode.com/problems/word-break-ii/

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */
var wordBreak = function(s, wordDict) {
    const words = new Set(wordDict);
    const memo = new Map();

    const dfs = (start) => {
        if (memo.has(start)) return memo.get(start);
        if (start === s.length) return [""];

        const sentences = [];
        for (let end = start + 1; end <= s.length; end += 1) {
            const word = s.slice(start, end);
            if (!words.has(word)) continue;

            for (const tail of dfs(end)) {
                sentences.push(tail ? `${word} ${tail}` : word);
            }
        }
        memo.set(start, sentences);
        return sentences;
    };

    return dfs(0);
};
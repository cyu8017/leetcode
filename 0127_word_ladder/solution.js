// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    const words = new Set(wordList);
    if (!words.has(endWord)) {
        return 0;
    }

    const queue = [[beginWord, 1]];
    const visited = new Set([beginWord]);
    let front = 0;

    while (front < queue.length) {
        const [word, steps] = queue[front++];
        if (word === endWord) {
            return steps;
        }

        for (let i = 0; i < word.length; i++) {
            for (let code = 97; code <= 122; code++) {
                const next = word.slice(0, i) + String.fromCharCode(code) + word.slice(i + 1);
                if (words.has(next) && !visited.has(next)) {
                    visited.add(next);
                    queue.push([next, steps + 1]);
                }
            }
        }
    }

    return 0;
};
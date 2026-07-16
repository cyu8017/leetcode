// LeetCode 0243 - Shortest Word Distance
// https://leetcode.com/problems/shortest-word-distance/

/**
 * @param {string[]} wordsDict
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var shortestWordDistance = function(wordsDict, word1, word2) {
    let index1 = -1;
    let index2 = -1;
    let best = Number.POSITIVE_INFINITY;
    for (let index = 0; index < wordsDict.length; index++) {
        const word = wordsDict[index];
        if (word === word1) {
            index1 = index;
            if (index2 >= 0) {
                best = Math.min(best, index - index2);
            }
        }
        if (word === word2) {
            index2 = index;
            if (index1 >= 0) {
                best = Math.min(best, index - index1);
            }
        }
    }
    return best;
};

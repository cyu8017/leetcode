// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

/**
 * @param {string[]} wordsDict
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var shortestWordDistance = function(wordsDict, word1, word2) {
    if (word1 === word2) {
        let previous = -1;
        let best = Number.POSITIVE_INFINITY;
        for (let index = 0; index < wordsDict.length; index++) {
            if (wordsDict[index] === word1) {
                if (previous >= 0) {
                    best = Math.min(best, index - previous);
                }
                previous = index;
            }
        }
        return best;
    }

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

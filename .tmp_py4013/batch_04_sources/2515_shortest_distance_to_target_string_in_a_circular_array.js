// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

/**
 * @param {string[]} words
 * @param {string} target
 * @param {number} startIndex
 * @return {number}
 */
var closestTarget = function(words, target, startIndex) {
    const n = words.length;
    let best = -1;
    for (let i = 0; i < n; i++) {
        if (words[i] === target) {
            let d = i - startIndex;
            if (d < 0) d = -d;
            if (n - d < d) d = n - d;
            if (best < 0 || d < best) best = d;
        }
    }
    return best;
};

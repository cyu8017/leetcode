// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

/**
 * // This is the InfiniteStream's API interface.
 * // You should not implement it, or speculate about its implementation
 * function InfiniteStream() {
 *     @param {number[]} bits
 *     InfiniteStream = function(bits) {
 *         ...
 *     };
 *
 *     @return {number}
 *     this.next = function() {
 *         ...
 *     };
 * };
 */
function getLPS(pattern) {
    const n = pattern.length;
    const lps = new Array(n).fill(0);
    let j = 0;
    for (let i = 1; i < n; i++) {
        while (j > 0 && pattern[j] !== pattern[i]) j = lps[j - 1];
        if (pattern[i] === pattern[j]) {
            j++;
            lps[i] = j;
        }
    }
    return lps;
}
var findPattern = function(stream, pattern) {
    const lps = getLPS(pattern);
    let i = 0, j = 0, bit = 0;
    let readNext = false;
    while (true) {
        if (!readNext) {
            bit = stream.next();
            readNext = true;
        }
        if (bit === pattern[j]) {
            i++;
            readNext = false;
            j++;
            if (j === pattern.length) return i - j;
        } else if (j > 0) {
            j = lps[j - 1];
        } else {
            i++;
            readNext = false;
        }
    }
};

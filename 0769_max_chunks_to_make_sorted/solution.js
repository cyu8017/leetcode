// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    let chunks = 0, maxSoFar = 0;
    for (let i = 0; i < arr.length; i++) {
        maxSoFar = Math.max(maxSoFar, arr[i]);
        if (maxSoFar === i) chunks++;
    }
    return chunks;
};

// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    let white = 0;
    for (let i = 0; i < k; i++) if (blocks[i] === 'W') white++;
    let ans = white;
    for (let i = k; i < blocks.length; i++) {
        if (blocks[i] === 'W') white++;
        if (blocks[i - k] === 'W') white--;
        ans = Math.min(ans, white);
    }
    return ans;
};

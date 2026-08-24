// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

/**
 * @param {number[]} stones
 * @return {number}
 */
var maxJump = function(stones) {
    let ans = stones[1] - stones[0];
    for (let i = 2; i < stones.length; i++) {
        const diff = stones[i] - stones[i - 2];
        if (diff > ans) ans = diff;
    }
    return ans;
};

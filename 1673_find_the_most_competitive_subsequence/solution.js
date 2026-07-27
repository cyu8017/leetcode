// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var mostCompetitive = function(nums, k) {
    const st = [];
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        while (st.length && st[st.length - 1] > x && st.length - 1 + nums.length - i >= k) st.pop();
        if (st.length < k) st.push(x);
    }
    return st;
};

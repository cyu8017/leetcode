// LeetCode 3719 - Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/

var longestBalanced = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const vis = new Set();
        const cnt = [0, 0];
        for (let j = i; j < n; j++) {
            if (!vis.has(nums[j])) {
                vis.add(nums[j]);
                cnt[nums[j] & 1]++;
            }
            if (cnt[0] === cnt[1]) ans = Math.max(ans, j - i + 1);
        }
    }
    return ans;
};

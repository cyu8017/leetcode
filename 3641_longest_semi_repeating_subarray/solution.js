// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

var longestSubarray = function(nums, k) {
    const cnt = new Map();
    let ans = 0, cur = 0, l = 0;
    for (let r = 0; r < nums.length; r++) {
        const c = (cnt.get(nums[r]) || 0) + 1;
        cnt.set(nums[r], c);
        if (c === 2) cur++;
        while (cur > k) {
            const c2 = (cnt.get(nums[l]) || 0) - 1;
            cnt.set(nums[l], c2);
            if (c2 === 1) cur--;
            l++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
};

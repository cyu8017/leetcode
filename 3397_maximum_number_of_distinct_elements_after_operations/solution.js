// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

var maxDistinctElements = function(nums, k) {
    nums = nums.slice().sort((a, b) => a - b);
    let ans = 0;
    let prev = Number.MIN_SAFE_INTEGER / 2;
    for (const x of nums) {
        let cur = x - k;
        if (cur <= prev) cur = prev + 1;
        if (cur > x + k) continue;
        ans++;
        prev = cur;
    }
    return ans;
};

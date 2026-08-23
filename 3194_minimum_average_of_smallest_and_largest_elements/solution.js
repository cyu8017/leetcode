// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

var minimumAverage = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let ans = 1 << 30;
    for (let i = 0; i < n / 2; i++) ans = Math.min(ans, nums[i] + nums[n - i - 1]);
    return ans / 2.0;
};

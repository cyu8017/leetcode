// LeetCode 3392 - Count Subarrays of Length Three With a Condition
// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

var countSubarrays = function(nums) {
    let ans = 0;
    for (let i = 0; i + 2 < nums.length; i++) {
        if (nums[i] * 2 + nums[i + 2] * 2 === nums[i + 1]) ans++;
    }
    return ans;
};

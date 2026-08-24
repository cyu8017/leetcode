// LeetCode 2302 - Count Subarrays With Score Less Than K
// https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

var countSubarrays = function(nums, k) {
    let ans = 0, sum = 0, left = 0;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum * (right - left + 1) >= k) {
            sum -= nums[left];
            left++;
        }
        ans += right - left + 1;
    }
    return ans;
};

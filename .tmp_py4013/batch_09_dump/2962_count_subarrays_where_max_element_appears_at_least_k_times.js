// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

var countSubarrays = function(nums, k) {
    let mx = nums[0];
    for (const v of nums) if (v > mx) mx = v;
    let ans = 0, cnt = 0, left = 0;
    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === mx) cnt++;
        while (cnt >= k) {
            if (nums[left] === mx) cnt--;
            left++;
        }
        ans += left;
    }
    return ans;
};

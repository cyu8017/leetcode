// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function(nums, goal) {
    const atMost = (g) => {
        if (g < 0) return 0;
        let left = 0, sum = 0, ans = 0;
        for (let right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum > g) sum -= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    };
    return atMost(goal) - atMost(goal - 1);
};

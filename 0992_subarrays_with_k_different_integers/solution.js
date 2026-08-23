// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraysWithKDistinct = function(nums, k) {
    const atMost = (m) => {
        if (m < 0) return 0;
        const count = new Map();
        let left = 0, ans = 0;
        for (let right = 0; right < nums.length; right++) {
            count.set(nums[right], (count.get(nums[right]) || 0) + 1);
            while (count.size > m) {
                const v = nums[left++];
                const nv = count.get(v) - 1;
                if (nv === 0) count.delete(v);
                else count.set(v, nv);
            }
            ans += right - left + 1;
        }
        return ans;
    };
    return atMost(k) - atMost(k - 1);
};

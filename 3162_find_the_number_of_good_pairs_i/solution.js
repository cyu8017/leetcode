// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, k) {
    let ans = 0;
    for (const x of nums1)
        for (const y of nums2)
            if (x % (y * k) === 0) ans++;
    return ans;
};

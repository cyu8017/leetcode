// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
var twoOutOfThree = function(nums1, nums2, nums3) {
    const s0 = new Set(nums1), s1 = new Set(nums2), s2 = new Set(nums3);
    const ans = [];
    for (let v = 1; v <= 100; v++) {
        const c = (s0.has(v) ? 1 : 0) + (s1.has(v) ? 1 : 0) + (s2.has(v) ? 1 : 0);
        if (c >= 2) ans.push(v);
    }
    return ans;
};

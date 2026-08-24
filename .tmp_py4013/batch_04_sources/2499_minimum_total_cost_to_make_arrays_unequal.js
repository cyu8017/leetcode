// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minimumTotalCost = function(nums1, nums2) {
    const n = nums1.length;
    const freq = new Map();
    let ans = 0, same = 0;
    for (let i = 0; i < n; i++) {
        if (nums1[i] === nums2[i]) {
            same++;
            freq.set(nums1[i], (freq.get(nums1[i]) || 0) + 1);
            ans += i;
        }
    }
    let maxFreq = 0, maxVal = 0;
    for (const [key, value] of freq) {
        if (value > maxFreq) {
            maxFreq = value;
            maxVal = key;
        }
    }
    let need = maxFreq * 2 - same;
    if (need <= 0) return ans;
    for (let i = 0; i < n && need > 0; i++) {
        if (nums1[i] !== nums2[i] && nums1[i] !== maxVal && nums2[i] !== maxVal) {
            ans += i;
            need--;
        }
    }
    return need > 0 ? -1 : ans;
};

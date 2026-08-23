// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var anagramMappings = function(nums1, nums2) {
    const positions = new Map();
    for (let i = 0; i < nums2.length; i++) {
        if (!positions.has(nums2[i])) positions.set(nums2[i], []);
        positions.get(nums2[i]).push(i);
    }
    const result = new Array(nums1.length);
    for (let i = 0; i < nums1.length; i++) result[i] = positions.get(nums1[i]).shift();
    return result;
};

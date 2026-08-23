// LeetCode 0349 - Intersection of Two Arrays
var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    return [...set1].filter((value) => set2.has(value));
};

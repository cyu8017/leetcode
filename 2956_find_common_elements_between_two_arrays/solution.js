// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

var findIntersectionValues = function(nums1, nums2) {
    const s1 = new Set(nums1);
    const s2 = new Set(nums2);
    let a = 0, b = 0;
    for (const v of nums1) if (s2.has(v)) a++;
    for (const v of nums2) if (s1.has(v)) b++;
    return [a, b];
};

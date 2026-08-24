// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

var maximumSetSize = function(nums1, nums2) {
    const s1 = new Set(nums1);
    const s2 = new Set(nums2);
    let a = 0, b = 0, c = 0;
    for (const x of s1) if (!s2.has(x)) a++;
    for (const x of s2) {
        if (!s1.has(x)) b++;
        else c++;
    }
    const n = nums1.length;
    a = Math.min(a, n / 2);
    b = Math.min(b, n / 2);
    return Math.min(a + b + c, n);
};

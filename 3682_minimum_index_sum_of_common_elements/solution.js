// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

var minimumSum = function(nums1, nums2) {
    const inf = 1 << 30;
    const d = new Map();
    for (let i = 0; i < nums2.length; i++)
        if (!d.has(nums2[i])) d.set(nums2[i], i);
    let ans = inf;
    for (let i = 0; i < nums1.length; i++) {
        if (d.has(nums1[i])) ans = Math.min(ans, i + d.get(nums1[i]));
    }
    return ans === inf ? -1 : ans;
};

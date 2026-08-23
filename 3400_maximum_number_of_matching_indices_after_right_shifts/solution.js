// LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
// https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

var maximumMatchingIndices = function(nums1, nums2) {
    const n = nums1.length;
    let ans = 0;
    for (let shift = 0; shift < n; shift++) {
        let cnt = 0;
        for (let i = 0; i < n; i++) {
            if (nums1[(i - shift + n) % n] === nums2[i]) cnt++;
        }
        if (cnt > ans) ans = cnt;
    }
    return ans;
};

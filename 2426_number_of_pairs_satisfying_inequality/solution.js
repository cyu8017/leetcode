// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} diff
 * @return {number}
 */
var numberOfPairs = function(nums1, nums2, diff) {
    const n = nums1.length;
    const arr = Array(n);
    const tmp = Array(n);
    for (let i = 0; i < n; i++) arr[i] = nums1[i] - nums2[i];
    const mergeCount = (l, r) => {
        if (r - l <= 1) return 0;
        const m = (l + r) >> 1;
        let ans = mergeCount(l, m) + mergeCount(m, r);
        let j = m;
        for (let i = l; i < m; i++) {
            while (j < r && arr[j] < arr[i] - diff) j++;
            ans += r - j;
        }
        let p = l, q = m, i2 = l;
        while (p < m && q < r) {
            if (arr[p] <= arr[q]) tmp[i2++] = arr[p++];
            else tmp[i2++] = arr[q++];
        }
        while (p < m) tmp[i2++] = arr[p++];
        while (q < r) tmp[i2++] = arr[q++];
        for (let t = l; t < r; t++) arr[t] = tmp[t];
        return ans;
    };
    return mergeCount(0, n);
};

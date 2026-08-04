// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumSum = function(arr) {
    let keep = arr[0], del = arr[0], ans = arr[0];
    for (let i = 1; i < arr.length; i++) {
        const x = arr[i];
        del = Math.max(keep, del + x);
        keep = Math.max(keep + x, x);
        ans = Math.max(ans, keep, del);
    }
    return ans;
};

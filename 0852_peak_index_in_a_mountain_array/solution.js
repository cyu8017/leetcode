// LeetCode 0852 - Peak Index in a Mountain Array
// https://leetcode.com/problems/peak-index-in-a-mountain-array/

/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    let lo = 0, hi = arr.length - 1;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (arr[mid] < arr[mid + 1]) lo = mid + 1;
        else hi = mid;
    }
    return lo;
};

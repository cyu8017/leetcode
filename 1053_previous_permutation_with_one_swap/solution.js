// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var prevPermOpt1 = function(arr) {
    const n = arr.length;
    let i = n - 2;
    while (i >= 0 && arr[i] <= arr[i + 1]) i--;
    if (i < 0) return arr;
    let j = n - 1;
    while (arr[j] >= arr[i] || arr[j] === arr[j - 1]) j--;
    const tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
    return arr;
};

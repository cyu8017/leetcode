// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

var filter = function(arr, fn) {
    const out = [];
    for (let i = 0; i < arr.length; i++) if (fn(arr[i], i)) out.push(arr[i]);
    return out;
};

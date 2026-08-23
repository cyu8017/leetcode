// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

var sortBy = function(arr, fn) {
    return arr.slice().sort((a, b) => fn(a) - fn(b));
};

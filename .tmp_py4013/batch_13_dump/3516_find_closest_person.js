// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

var findClosest = function(x, y, z) {
    const a = Math.abs(x - z), b = Math.abs(y - z);
    if (a === b) return 0;
    return a < b ? 1 : 2;
};

// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

var isZeroArray = function(nums, queries) {
    const n = nums.length;
    const diff = new Array(n + 1).fill(0);
    for (const q of queries) {
        diff[q[0]]++;
        diff[q[1] + 1]--;
    }
    let cur = 0;
    for (let i = 0; i < n; i++) {
        cur += diff[i];
        if (cur < nums[i]) return false;
    }
    return true;
};

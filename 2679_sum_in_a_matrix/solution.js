// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

var matrixSum = function(nums) {
    for (const row of nums) row.sort((a, b) => a - b);
    let ans = 0;
    const n = nums[0].length;
    for (let j = 0; j < n; j++) {
        let mx = 0;
        for (const row of nums) mx = Math.max(mx, row[j]);
        ans += mx;
    }
    return ans;
};

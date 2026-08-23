// LeetCode 3567 - Minimum Absolute Difference in Sliding Submatrix
// https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

var minAbsDiff = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const ans = Array.from({length: m - k + 1}, () => new Array(n - k + 1).fill(0));
    for (let i = 0; i <= m - k; i++) {
        for (let j = 0; j <= n - k; j++) {
            const nums = [];
            for (let x = i; x < i + k; x++)
                for (let y = j; y < j + k; y++) nums.push(grid[x][y]);
            nums.sort((a, b) => a - b);
            let d = 2147483647;
            for (let t = 1; t < nums.length; t++) {
                if (nums[t] !== nums[t - 1]) d = Math.min(d, Math.abs(nums[t] - nums[t - 1]));
            }
            if (d !== 2147483647) ans[i][j] = d;
        }
    }
    return ans;
};

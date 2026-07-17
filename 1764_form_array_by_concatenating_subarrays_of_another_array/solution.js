// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

/**
 * @param {number[][]} groups
 * @param {number[]} nums
 * @return {boolean}
 */
var canChoose = function(groups, nums) {
    const n = nums.length;
    const matches = (start, g) => {
        for (let t = 0; t < g.length; t++) {
            if (nums[start + t] !== g[t]) {
                return false;
            }
        }
        return true;
    };
    const dfs = (i, start) => {
        if (i === groups.length) {
            return start === n;
        }
        const m = groups[i].length;
        for (let j = start; j <= n - m; j++) {
            if (matches(j, groups[i]) && dfs(i + 1, j + m)) {
                return true;
            }
        }
        return false;
    };
    return dfs(0, 0);
};

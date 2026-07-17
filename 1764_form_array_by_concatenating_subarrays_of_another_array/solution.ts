// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

function canChoose(groups: number[][], nums: number[]): boolean {
    const n = nums.length;
    const matches = (start: number, g: number[]): boolean => {
        for (let t = 0; t < g.length; t++) {
            if (nums[start + t] !== g[t]) {
                return false;
            }
        }
        return true;
    };
    const dfs = (i: number, start: number): boolean => {
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
}

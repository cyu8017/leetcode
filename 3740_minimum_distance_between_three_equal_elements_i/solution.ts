// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum_distance_between_three_equal_elements_i/

export function minimumDistance(nums: any): any {
    const g = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (!g.has(nums[i])) g.set(nums[i], []);
        g.get(nums[i]).push(i);
    }
    const inf = 1 << 30;
    let ans = inf;
    for (const ls of g.values()) {
        const m = ls.length;
        for (let h = 0; h < m - 2; h++) {
            ans = Math.min(ans, (ls[h + 2] - ls[h]) * 2);
        }
    }
    return ans === inf ? -1 : ans;
}

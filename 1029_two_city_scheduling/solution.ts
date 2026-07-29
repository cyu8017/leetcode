// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

function twoCitySchedCost(costs: number[][]): number {
    costs.sort((a, b) => (a[0] - a[1]) - (b[0] - b[1]));
    const n = costs.length / 2;
    let ans = 0;
    for (let i = 0; i < n; i++) ans += costs[i][0];
    for (let i = n; i < costs.length; i++) ans += costs[i][1];
    return ans;
}

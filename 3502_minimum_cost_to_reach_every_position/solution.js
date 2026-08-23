// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

var minCosts = function(cost) {
    const n = cost.length;
    const ans = new Array(n);
    let mi = cost[0];
    for (let i = 0; i < n; i++) {
        mi = Math.min(mi, cost[i]);
        ans[i] = mi;
    }
    return ans;
};

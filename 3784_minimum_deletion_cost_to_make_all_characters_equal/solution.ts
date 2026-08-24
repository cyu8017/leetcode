// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum_deletion_cost_to_make_all_characters_equal/

export function minCost(s: any, cost: any): any {
    let tot = 0;
    const g = new Map();
    for (let i = 0; i < cost.length; i++) {
        tot += cost[i];
        g.set(s[i], (g.get(s[i]) || 0) + cost[i]);
    }
    let ans = tot;
    for (const x of g.values()) ans = Math.min(ans, tot - x);
    return ans;
}

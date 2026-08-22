// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

function maxIceCream(costs: number[], coins: number): number {
    costs = [...costs].sort((a, b) => a - b);
    let count = 0;
    for (const cost of costs) {
        if (coins < cost) break;
        coins -= cost;
        count += 1;
    }
    return count;
}

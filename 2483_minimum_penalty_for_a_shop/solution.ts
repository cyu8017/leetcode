// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

export function bestClosingTime(customers: string): number {
    const n = customers.length;
    let penalty = 0;
    for (const c of customers) if (c === 'Y') penalty++;
    let best = penalty, ans = 0;
    for (let i = 0; i < n; i++) {
        if (customers[i] === 'Y') penalty--;
        else penalty++;
        if (penalty < best) {
            best = penalty;
            ans = i + 1;
        }
    }
    return ans;
}

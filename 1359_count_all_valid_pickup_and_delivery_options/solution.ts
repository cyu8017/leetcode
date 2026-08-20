// LeetCode 1359 - Count All Valid Pickup And Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

function countOrders(n: number): number {
    let ans = 1;
    const mod = 1000000007;
    for (let i = 1; i <= n; i++) ans = ans * i * (2 * i - 1) % mod;
    return ans;
}

// LeetCode 3638 - Maximum Balanced Shipments
// https://leetcode.com/problems/maximum-balanced-shipments/

export function maxBalancedShipments(weight: any): any {
    let ans = 0, mx = 0;
    for (const x of weight) {
        mx = Math.max(mx, x);
        if (x < mx) {
            ans++;
            mx = 0;
        }
    }
    return ans;
}

// LeetCode 1359 - Count All Valid Pickup and Delivery Options
// https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

int countOrders(int n) {
    long long ans = 1;
    const int MOD = 1000000007;
    for (int i = 1; i <= n; i++) {
        ans = ans * i % MOD;
        ans = ans * (2 * i - 1) % MOD;
    }
    return (int)ans;
}

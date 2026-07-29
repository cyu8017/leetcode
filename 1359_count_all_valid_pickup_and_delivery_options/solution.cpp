class Solution {
public:
    int countOrders(int n) {
        long long ans = 1;
        const int mod = 1000000007;
        for (int i = 1; i <= n; ++i) ans = ans * i * (2 * i - 1) % mod;
        return (int)ans;
    }
};

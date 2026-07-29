class Solution {
public:
    int numOfWays(int n) {
        const int mod = 1000000007;
        long long aba = 6, abc = 6;
        for (int i = 1; i < n; ++i) {
            long long naba = (3 * aba + 2 * abc) % mod;
            long long nab = (2 * aba + 2 * abc) % mod;
            aba = naba; abc = nab;
        }
        return (int)((aba + abc) % mod);
    }
};

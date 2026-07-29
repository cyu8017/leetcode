#include <cstring>
#include <string>
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;
    int n, m;
    std::string s1, s2, evil;
    std::vector<std::vector<int>> trans;
    int memo[501][51][2][2];
    int dp(int i, int j, int lo, int hi) {
        if (j == m) return 0;
        if (i == n) return 1;
        int& res = memo[i][j][lo][hi];
        if (res != -1) return res;
        int a = lo ? s1[i] - 'a' : 0;
        int b = hi ? s2[i] - 'a' : 25;
        long long ans = 0;
        for (int x = a; x <= b; ++x)
            ans += dp(i + 1, trans[j][x], lo && x == a, hi && x == b);
        return res = (int)(ans % MOD);
    }
public:
    int findGoodStrings(int n_, std::string s1_, std::string s2_, std::string evil_) {
        n = n_; s1 = s1_; s2 = s2_; evil = evil_; m = (int)evil.size();
        std::vector<int> pi(m, 0);
        for (int i = 1; i < m; ++i) {
            int j = pi[i - 1];
            while (j && evil[i] != evil[j]) j = pi[j - 1];
            if (evil[i] == evil[j]) ++j;
            pi[i] = j;
        }
        trans.assign(m, std::vector<int>(26, 0));
        for (int j = 0; j < m; ++j) {
            for (int x = 0; x < 26; ++x) {
                char c = char('a' + x);
                int k = j;
                while (k && evil[k] != c) k = pi[k - 1];
                if (evil[k] == c) ++k;
                trans[j][x] = k;
            }
        }
        std::memset(memo, -1, sizeof(memo));
        return dp(0, 0, 1, 1);
    }
};

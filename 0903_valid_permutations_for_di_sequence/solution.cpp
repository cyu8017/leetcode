// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

#include <string>
#include <vector>

class Solution {
public:
    int numPermsDISequence(std::string s) {
        const int MOD = 1000000007;
        int n = (int)s.size();
        std::vector<int> dp(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            std::vector<int> newDp(n + 1, 0);
            if (s[i - 1] == 'I') {
                int postfix = 0;
                for (int j = n - i; j >= 0; j--) {
                    postfix = (postfix + dp[j + 1]) % MOD;
                    newDp[j] = postfix;
                }
            } else {
                int prefix = 0;
                for (int j = 0; j <= n - i; j++) {
                    prefix = (prefix + dp[j]) % MOD;
                    newDp[j] = prefix;
                }
            }
            dp.swap(newDp);
        }
        return dp[0];
    }
};

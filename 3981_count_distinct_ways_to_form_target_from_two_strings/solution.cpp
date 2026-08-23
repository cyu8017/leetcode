// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

#include <string>
#include <vector>

class Solution {
public:
    int countWays(std::string word1, std::string word2, std::string target) {
        const int mod = 1000000007;
        int n1 = (int)word1.size();
        int n2 = (int)word2.size();
        int size = (n1 + 1) * (n2 + 1) * 4;
        auto index = [&](int i, int j, int mask) {
            return ((i * (n2 + 1) + j) * 4) + mask;
        };
        std::vector<int> dp(size, 0), next(size, 0);
        dp[index(0, 0, 0)] = 1;
        for (char ch : target) {
            std::fill(next.begin(), next.end(), 0);
            for (int j = 0; j <= n2; j++) {
                int prefix[4] = {0, 0, 0, 0};
                for (int a = 0; a < n1; a++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(a, j, mask)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word1[a] == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = index(a + 1, j, mask | 1);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            for (int i = 0; i <= n1; i++) {
                int prefix[4] = {0, 0, 0, 0};
                for (int b = 0; b < n2; b++) {
                    for (int mask = 0; mask < 4; mask++) {
                        prefix[mask] += dp[index(i, b, mask)];
                        if (prefix[mask] >= mod) prefix[mask] -= mod;
                    }
                    if (word2[b] == ch) {
                        for (int mask = 0; mask < 4; mask++) {
                            int at = index(i, b + 1, mask | 2);
                            next[at] += prefix[mask];
                            if (next[at] >= mod) next[at] -= mod;
                        }
                    }
                }
            }
            dp.swap(next);
        }
        int answer = 0;
        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) {
                answer += dp[index(i, j, 3)];
                if (answer >= mod) answer -= mod;
            }
        }
        return answer;
    }
};

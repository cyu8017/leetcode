// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

#include <algorithm>
#include <climits>
#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::string word1, std::string word2) {
        int n = (int)word1.size();
        std::vector<int> f(n + 1, INT_MAX / 2);
        f[0] = 0;
        auto calc = [&](int l, int r, bool rev) {
            int cnt[26][26] = {};
            int res = 0;
            for (int i = l; i <= r; i++) {
                int j = rev ? r - (i - l) : i;
                int a = word1[j] - 'a';
                int b = word2[i] - 'a';
                if (a != b) {
                    if (cnt[b][a] > 0) cnt[b][a]--;
                    else {
                        cnt[a][b]++;
                        res++;
                    }
                }
            }
            return res;
        };
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int a = calc(j, i - 1, false);
                int b = 1 + calc(j, i - 1, true);
                f[i] = std::min(f[i], f[j] + std::min(a, b));
            }
        }
        return f[n];
    }
};

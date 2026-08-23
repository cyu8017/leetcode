// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

#include <string>
#include <vector>
#include <unordered_map>
#include <array>
#include <algorithm>

class Solution {
public:
    int minimumSubstringsInPartition(std::string s) {
        int n = (int)s.size();
        std::vector<int> memo(n, -1);
        auto dfs = [&](auto&& self, int i) -> int {
            if (i >= n) return 0;
            if (memo[i] != -1) return memo[i];
            std::array<int, 26> cnt{};
            std::unordered_map<int, int> freq;
            memo[i] = n - i;
            for (int j = i; j < n; j++) {
                int k = s[j] - 'a';
                if (cnt[k] > 0) {
                    if (--freq[cnt[k]] == 0) freq.erase(cnt[k]);
                }
                cnt[k]++;
                freq[cnt[k]]++;
                if ((int)freq.size() == 1) {
                    memo[i] = std::min(memo[i], 1 + self(self, j + 1));
                }
            }
            return memo[i];
        };
        return dfs(dfs, 0);
    }
};

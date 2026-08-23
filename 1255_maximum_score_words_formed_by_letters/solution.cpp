// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxScoreWords(std::vector<std::string>& words, std::vector<char>& letters, std::vector<int>& score) {
        std::vector<int> available(26, 0);
        for (char ch : letters) {
            ++available[ch - 'a'];
        }
        const int n = static_cast<int>(words.size());
        std::vector<std::vector<int>> counts(n, std::vector<int>(26, 0));
        std::vector<int> values(n, 0);
        for (int i = 0; i < n; ++i) {
            for (char ch : words[i]) {
                ++counts[i][ch - 'a'];
                values[i] += score[ch - 'a'];
            }
        }
        auto dfs = [&](auto&& self, int i) -> int {
            if (i == n) {
                return 0;
            }
            int best = self(self, i + 1);
            bool ok = true;
            for (int c = 0; c < 26; ++c) {
                if (counts[i][c] > available[c]) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                for (int c = 0; c < 26; ++c) {
                    available[c] -= counts[i][c];
                }
                best = std::max(best, values[i] + self(self, i + 1));
                for (int c = 0; c < 26; ++c) {
                    available[c] += counts[i][c];
                }
            }
            return best;
        };
        return dfs(dfs, 0);
    }
};

// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

#include <string>
#include <vector>

class Solution {
    bool canFinish(const std::string& w1, const std::string& w2, int i, int j, bool usedSkip, const std::vector<int>& right) {
        int m = (int)w2.size();
        if (j >= m) return true;
        if (!usedSkip) {
            if (right[j] >= i) return true;
            if (j + 1 <= m && right[j + 1] > i) return true;
            if (right[j] > i) return true;
            return false;
        }
        return right[j] >= i;
    }

public:
    std::vector<int> validSequence(std::string word1, std::string word2) {
        int n = (int)word1.size(), m = (int)word2.size();
        std::vector<int> right(m + 1);
        right[m] = n;
        int j = m - 1;
        for (int i = n - 1; i >= 0 && j >= 0; i--) {
            if (word1[i] == word2[j]) {
                right[j] = i;
                j--;
            }
        }
        for (; j >= 0; j--) right[j] = -1;
        std::vector<int> ans(m);
        bool usedSkip = false;
        int i = 0;
        for (j = 0; j < m; j++) {
            bool found = false;
            while (i < n) {
                if (word1[i] == word2[j]) {
                    if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
                        ans[j] = i; i++; found = true; break;
                    }
                } else if (!usedSkip) {
                    if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
                        ans[j] = i; i++; usedSkip = true; found = true; break;
                    }
                }
                i++;
            }
            if (!found) return {};
        }
        return ans;
    }
};

// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

#include <vector>

class Solution {
public:
    std::vector<int> constructDistancedSequence(int n) {
        std::vector<int> ans(2 * n - 1, 0);
        std::vector<bool> used(n + 1, false);
        backtrack(0, n, ans, used);
        return ans;
    }

private:
    bool backtrack(int i, int n, std::vector<int>& ans, std::vector<bool>& used) {
        while (i < (int)ans.size() && ans[i] != 0) {
            i++;
        }
        if (i == (int)ans.size()) {
            return true;
        }
        for (int value = n; value >= 1; value--) {
            if (used[value]) {
                continue;
            }
            if (value == 1) {
                ans[i] = 1;
                used[1] = true;
                if (backtrack(i + 1, n, ans, used)) {
                    return true;
                }
                used[1] = false;
                ans[i] = 0;
            } else {
                int j = i + value;
                if (j < (int)ans.size() && ans[j] == 0) {
                    ans[i] = value;
                    ans[j] = value;
                    used[value] = true;
                    if (backtrack(i + 1, n, ans, used)) {
                        return true;
                    }
                    used[value] = false;
                    ans[i] = 0;
                    ans[j] = 0;
                }
            }
        }
        return false;
    }
};

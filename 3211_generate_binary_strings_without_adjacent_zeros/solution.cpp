// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> validStrings(int n) {
        std::vector<std::string> ans;
        std::string t;
        auto dfs = [&](auto&& self, int i) -> void {
            if (i >= n) { ans.push_back(t); return; }
            for (int j = 0; j < 2; j++) {
                if ((j == 0 && (i == 0 || t[i - 1] == '1')) || j == 1) {
                    t.push_back(char('0' + j));
                    self(self, i + 1);
                    t.pop_back();
                }
            }
        };
        dfs(dfs, 0);
        return ans;
    }
};

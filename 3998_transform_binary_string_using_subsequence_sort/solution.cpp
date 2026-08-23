// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<bool> transformStr(std::string s, std::vector<std::string>& strs) {
        int n = (int)s.size();
        std::vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (s[i] == '1' ? 1 : 0);
        std::vector<bool> result(strs.size());
        for (int i = 0; i < (int)strs.size(); i++) {
            int left = 0, right = 0;
            bool ok = true;
            for (int j = 0; j < n; j++) {
                left += (strs[i][j] == '1' ? 1 : 0);
                int add = (strs[i][j] != '0' ? 1 : 0);
                right = right + add;
                if (right > prefix[j + 1]) right = prefix[j + 1];
                if (left > right) {
                    ok = false;
                    break;
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right;
        }
        return result;
    }
};

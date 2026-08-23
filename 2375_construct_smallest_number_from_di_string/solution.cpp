// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string smallestNumber(std::string pattern) {
        int n = (int)pattern.size();
        std::string ans(n + 1, '0');
        for (int i = 0; i <= n; i++) ans[i] = char('1' + i);
        int i = 0;
        while (i < n) {
            if (pattern[i] == 'I') {
                i++;
                continue;
            }
            int j = i;
            while (j < n && pattern[j] == 'D') j++;
            std::reverse(ans.begin() + i, ans.begin() + j + 1);
            i = j;
        }
        return ans;
    }
};

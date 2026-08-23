// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minimumOperations(std::string num) {
        int n = (int)num.size();
        int ans = n;
        bool has0 = false;
        for (char c : num) if (c == '0') has0 = true;
        if (has0) ans = std::min(ans, n - 1);
        std::vector<std::string> targets = {"00", "25", "50", "75"};
        for (auto& t : targets) {
            int j = n - 1;
            while (j >= 0 && num[j] != t[1]) j--;
            if (j < 0) continue;
            int i = j - 1;
            while (i >= 0 && num[i] != t[0]) i--;
            if (i < 0) continue;
            ans = std::min(ans, n - i - 2);
        }
        return ans;
    }
};

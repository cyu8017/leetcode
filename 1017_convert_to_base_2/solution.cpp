// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string baseNeg2(int n) {
        if (n == 0) return "0";
        std::string ans;
        while (n) {
            int rem = n % -2;
            n /= -2;
            if (rem < 0) {
                ++n;
                rem += 2;
            }
            ans.push_back(static_cast<char>('0' + rem));
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};


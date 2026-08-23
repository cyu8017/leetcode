// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

#include <vector>
#include <string>

class Solution {
public:
    int countSeniors(std::vector<std::string>& details) {
        int ans = 0;
        for (auto& d : details) {
            int age = (d[11] - '0') * 10 + (d[12] - '0');
            if (age > 60) ans++;
        }
        return ans;
    }
};

// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

#include <string>
#include <vector>

class Solution {
public:
    int numWays(std::string s) {
        constexpr int MOD = 1000000007;
        int ones = 0;
        for (char ch : s) {
            if (ch == '1') {
                ++ones;
            }
        }
        if (ones % 3) {
            return 0;
        }
        if (ones == 0) {
            const long long gaps = static_cast<long long>(s.size()) - 1;
            return static_cast<int>(gaps * (gaps - 1) / 2 % MOD);
        }
        const int target = ones / 3;
        std::vector<int> positions;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            if (s[i] == '1') {
                positions.push_back(i);
            }
        }
        return static_cast<int>(
            static_cast<long long>(positions[target] - positions[target - 1]) *
            (positions[2 * target] - positions[2 * target - 1]) % MOD);
    }
};

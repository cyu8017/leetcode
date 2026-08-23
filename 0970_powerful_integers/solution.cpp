// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> powerfulIntegers(int x, int y, int bound) {
        std::unordered_set<int> ans;
        for (long long a = 1; a < bound; a *= x) {
            for (long long b = 1; a + b <= bound; b *= y) {
                ans.insert((int)(a + b));
                if (y == 1) break;
            }
            if (x == 1) break;
        }
        return std::vector<int>(ans.begin(), ans.end());
    }
};

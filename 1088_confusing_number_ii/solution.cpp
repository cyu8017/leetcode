// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int confusingNumberII(int n) {
        static const std::unordered_map<int, int> rotate = {
            {0, 0}, {1, 1}, {6, 9}, {8, 8}, {9, 6}};
        static const std::vector<int> digits = {0, 1, 6, 8, 9};
        int ans = 0;

        auto isConfusing = [&](long long num) {
            long long original = num;
            long long rotated = 0;
            while (num) {
                int d = static_cast<int>(num % 10);
                rotated = rotated * 10 + rotate.at(d);
                num /= 10;
            }
            return rotated != original;
        };

        std::function<void(long long)> dfs = [&](long long cur) {
            if (cur > n) {
                return;
            }
            if (cur && isConfusing(cur)) {
                ++ans;
            }
            if (cur == 0) {
                for (int d : {1, 6, 8, 9}) {
                    dfs(d);
                }
            } else {
                for (int d : digits) {
                    dfs(cur * 10 + d);
                }
            }
        };

        dfs(0);
        return ans;
    }
};

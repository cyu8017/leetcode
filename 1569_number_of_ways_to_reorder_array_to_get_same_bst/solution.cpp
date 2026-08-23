// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

#include <functional>
#include <vector>

class Solution {
public:
    int numOfWays(std::vector<int>& nums) {
        constexpr int MOD = 1000000007;
        const int n = static_cast<int>(nums.size());
        std::vector<std::vector<long long>> choose(n + 1, std::vector<long long>(n + 1, 0));
        for (int i = 0; i <= n; ++i) {
            choose[i][0] = choose[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD;
            }
        }

        std::function<long long(const std::vector<int>&)> ways =
            [&](const std::vector<int>& values) -> long long {
            if (static_cast<int>(values.size()) < 3) {
                return 1;
            }
            std::vector<int> left;
            std::vector<int> right;
            for (size_t i = 1; i < values.size(); ++i) {
                if (values[i] < values[0]) {
                    left.push_back(values[i]);
                } else {
                    right.push_back(values[i]);
                }
            }
            return choose[static_cast<int>(values.size()) - 1][static_cast<int>(left.size())] *
                   ways(left) % MOD * ways(right) % MOD;
        };

        return static_cast<int>((ways(nums) - 1 + MOD) % MOD);
    }
};

// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

#include <unordered_set>
#include <vector>

class Solution {
public:
    bool splitArray(std::vector<int>& nums) {
        const int n = static_cast<int>(nums.size());
        if (n < 7) {
            return false;
        }

        std::vector<long long> prefix(n + 1, 0);
        for (int index = 0; index < n; ++index) {
            prefix[index + 1] = prefix[index] + nums[index];
        }

        for (int j = 3; j < n - 3; ++j) {
            std::unordered_set<long long> seen;
            for (int i = 1; i < j - 1; ++i) {
                const long long first = prefix[i] - prefix[0];
                const long long second = prefix[j] - prefix[i + 1];
                if (first == second) {
                    seen.insert(first);
                }
            }

            for (int k = j + 2; k < n - 1; ++k) {
                const long long third = prefix[k] - prefix[j + 1];
                const long long fourth = prefix[n] - prefix[k + 1];
                if (third == fourth && seen.count(third)) {
                    return true;
                }
            }
        }

        return false;
    }
};

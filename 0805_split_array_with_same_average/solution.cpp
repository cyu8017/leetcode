// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

#include <algorithm>
#include <functional>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool splitArraySameAverage(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int total = 0;
        for (int x : nums) {
            total += x;
        }
        std::sort(nums.begin(), nums.end());

        std::unordered_set<long long> memo;
        std::function<bool(int, int, int)> find =
            [&](int target, int count, int index) -> bool {
            if (count == 0) {
                return target == 0;
            }
            if (index == n || count + index > n || target < 0) {
                return false;
            }
            long long key = (static_cast<long long>(target) << 20) |
                            (static_cast<long long>(count) << 10) | index;
            if (memo.count(key)) {
                return false;
            }
            if (find(target - nums[index], count - 1, index + 1) ||
                find(target, count, index + 1)) {
                return true;
            }
            memo.insert(key);
            return false;
        };

        for (int size = 1; size < n; ++size) {
            if (total * size % n == 0 && find(total * size / n, size, 0)) {
                return true;
            }
        }
        return false;
    }
};

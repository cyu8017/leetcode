// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

#include <algorithm>
#include <vector>

class Solution {
public:
    int bestRotation(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        std::vector<int> change(n, 1);
        for (int i = 0; i < n; ++i) {
            change[(i - nums[i] + 1 + n) % n] -= 1;
        }
        for (int i = 1; i < n; ++i) {
            change[i] += change[i - 1];
        }
        return static_cast<int>(std::max_element(change.begin(), change.end()) - change.begin());
    }
};

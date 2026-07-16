// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

#include <algorithm>
#include <vector>

class Solution {
    std::vector<std::vector<std::vector<int>>> memo_;

    int dp(int left, int right, int streak, const std::vector<int>& boxes) {
        if (left > right) {
            return 0;
        }
        if (memo_[left][right][streak] >= 0) {
            return memo_[left][right][streak];
        }

        while (right > left && boxes[right] == boxes[right - 1]) {
            right -= 1;
            streak += 1;
        }

        int best = (streak + 1) * (streak + 1) + dp(left, right - 1, 0, boxes);
        for (int index = left; index < right; ++index) {
            if (boxes[index] == boxes[right]) {
                best = std::max(
                    best,
                    dp(left, index, streak + 1, boxes) + dp(index + 1, right - 1, 0, boxes));
            }
        }

        memo_[left][right][streak] = best;
        return best;
    }

public:
    int removeBoxes(std::vector<int>& boxes) {
        const int n = static_cast<int>(boxes.size());
        memo_.assign(n, std::vector<std::vector<int>>(n, std::vector<int>(n + 1, -1)));
        return dp(0, n - 1, 0, boxes);
    }
};

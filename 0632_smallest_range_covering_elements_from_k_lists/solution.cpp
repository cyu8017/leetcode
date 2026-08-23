// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

#include <climits>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> smallestRange(std::vector<std::vector<int>>& nums) {
        using Node = std::tuple<int, int, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<Node>> heap;
        int currentMax = INT_MIN;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            heap.emplace(nums[i][0], i, 0);
            currentMax = std::max(currentMax, nums[i][0]);
        }
        int bestLeft = std::get<0>(heap.top());
        int bestRight = currentMax;
        while (true) {
            auto [value, listIndex, index] = heap.top();
            heap.pop();
            if (currentMax - value < bestRight - bestLeft) {
                bestLeft = value;
                bestRight = currentMax;
            }
            if (index + 1 == static_cast<int>(nums[listIndex].size())) {
                break;
            }
            const int nxt = nums[listIndex][index + 1];
            heap.emplace(nxt, listIndex, index + 1);
            currentMax = std::max(currentMax, nxt);
        }
        return {bestLeft, bestRight};
    }
};

// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> removeInterval(std::vector<std::vector<int>>& intervals,
                                                 std::vector<int>& toBeRemoved) {
        int left = toBeRemoved[0], right = toBeRemoved[1];
        std::vector<std::vector<int>> answer;
        for (const auto& interval : intervals) {
            int start = interval[0], end = interval[1];
            if (end <= left || start >= right) {
                answer.push_back({start, end});
            } else {
                if (start < left) {
                    answer.push_back({start, left});
                }
                if (end > right) {
                    answer.push_back({right, end});
                }
            }
        }
        return answer;
    }
};

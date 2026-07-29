// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

#include <algorithm>
#include <vector>

class Solution {
public:
    int intersectionSizeTwo(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            if (a[1] != b[1]) {
                return a[1] < b[1];
            }
            return a[0] < b[0];
        });
        int size = 0;
        int first = -1;
        int second = -1;
        for (const auto& interval : intervals) {
            int left = interval[0];
            int right = interval[1];
            if (left <= first) {
                continue;
            }
            if (left <= second) {
                ++size;
                first = second;
                second = right;
            } else {
                size += 2;
                first = right - 1;
                second = right;
            }
        }
        return size;
    }
};

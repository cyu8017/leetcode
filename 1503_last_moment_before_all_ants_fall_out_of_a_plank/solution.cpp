// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

#include <algorithm>
#include <vector>

class Solution {
public:
    int getLastMoment(int n, std::vector<int>& left, std::vector<int>& right) {
        int answer = 0;
        if (!left.empty()) {
            answer = std::max(answer, *std::max_element(left.begin(), left.end()));
        }
        if (!right.empty()) {
            answer = std::max(answer, n - *std::min_element(right.begin(), right.end()));
        }
        return answer;
    }
};

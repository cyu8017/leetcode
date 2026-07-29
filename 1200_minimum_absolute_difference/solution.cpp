// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> minimumAbsDifference(std::vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        int best = INT_MAX;
        for (int i = 0; i + 1 < static_cast<int>(arr.size()); ++i) {
            best = std::min(best, arr[i + 1] - arr[i]);
        }
        std::vector<std::vector<int>> answer;
        for (int i = 0; i + 1 < static_cast<int>(arr.size()); ++i) {
            if (arr[i + 1] - arr[i] == best) {
                answer.push_back({arr[i], arr[i + 1]});
            }
        }
        return answer;
    }
};

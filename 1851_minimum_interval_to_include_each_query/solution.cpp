// LeetCode 1851 - Minimum Interval to Include Each Query
// https://leetcode.com/problems/minimum-interval-to-include-each-query/

#include <algorithm>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> minInterval(std::vector<std::vector<int>>& intervals, std::vector<int>& queries) {
        std::sort(intervals.begin(), intervals.end());
        std::vector<std::pair<int, int>> indexed;
        indexed.reserve(queries.size());
        for (int i = 0; i < static_cast<int>(queries.size()); i++) {
            indexed.push_back({queries[i], i});
        }
        std::sort(indexed.begin(), indexed.end());

        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> heap;
        std::vector<int> answer(queries.size(), -1);
        int intervalIdx = 0;

        for (const auto& [query, queryIdx] : indexed) {
            while (intervalIdx < static_cast<int>(intervals.size()) && intervals[intervalIdx][0] <= query) {
                int left = intervals[intervalIdx][0];
                int right = intervals[intervalIdx][1];
                heap.push({right - left + 1, right});
                intervalIdx++;
            }
            while (!heap.empty() && heap.top().second < query) {
                heap.pop();
            }
            if (!heap.empty()) {
                answer[queryIdx] = heap.top().first;
            }
        }
        return answer;
    }
};

// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int scheduleCourse(std::vector<std::vector<int>>& courses) {
        std::sort(courses.begin(), courses.end(),
                  [](const std::vector<int>& a, const std::vector<int>& b) {
                      return a[1] < b[1];
                  });
        std::priority_queue<int> heap;
        int time = 0;
        for (const auto& course : courses) {
            const int duration = course[0];
            const int lastDay = course[1];
            if (time + duration <= lastDay) {
                heap.push(duration);
                time += duration;
            } else if (!heap.empty() && heap.top() > duration) {
                time += duration - heap.top();
                heap.pop();
                heap.push(duration);
            }
        }
        return static_cast<int>(heap.size());
    }
};

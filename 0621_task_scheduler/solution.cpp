// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

#include <algorithm>
#include <vector>

class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
        int counts[26] = {};
        for (char task : tasks) {
            ++counts[task - 'A'];
        }
        int maxFreq = 0;
        for (int count : counts) {
            maxFreq = std::max(maxFreq, count);
        }
        int maxCount = 0;
        for (int count : counts) {
            if (count == maxFreq) {
                ++maxCount;
            }
        }
        return std::max(
            static_cast<int>(tasks.size()),
            (maxFreq - 1) * (n + 1) + maxCount);
    }
};

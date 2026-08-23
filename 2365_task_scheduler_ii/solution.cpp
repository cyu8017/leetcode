// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long taskSchedulerII(std::vector<int>& tasks, int space) {
        std::unordered_map<int, long long> next;
        long long day = 0;
        for (int t : tasks) {
            if (next[t] > day) day = next[t];
            day++;
            next[t] = day + space;
        }
        return day;
    }
};

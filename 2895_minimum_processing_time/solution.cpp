// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minProcessingTime(std::vector<int>& processorTime, std::vector<int>& tasks) {
        std::sort(processorTime.begin(), processorTime.end());
        std::sort(tasks.begin(), tasks.end(), std::greater<int>());
        int ans = 0;
        for (int i = 0; i < (int)processorTime.size(); i++) {
            int fin = processorTime[i] + tasks[i * 4];
            if (fin > ans) ans = fin;
        }
        return ans;
    }
};

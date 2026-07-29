// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

#include <vector>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        std::vector<int> answer(temperatures.size(), 0);
        std::vector<int> stack;
        for (int i = 0; i < static_cast<int>(temperatures.size()); ++i) {
            while (!stack.empty() && temperatures[stack.back()] < temperatures[i]) {
                int prev = stack.back();
                stack.pop_back();
                answer[prev] = i - prev;
            }
            stack.push_back(i);
        }
        return answer;
    }
};

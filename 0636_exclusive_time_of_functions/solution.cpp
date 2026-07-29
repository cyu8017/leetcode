// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> exclusiveTime(int n, std::vector<std::string>& logs) {
        std::vector<int> result(n, 0);
        std::vector<int> stack;
        int prevTime = 0;
        for (const std::string& log : logs) {
            std::stringstream ss(log);
            std::string funcIdStr;
            std::string event;
            std::string timeStr;
            std::getline(ss, funcIdStr, ':');
            std::getline(ss, event, ':');
            std::getline(ss, timeStr, ':');
            const int funcId = std::stoi(funcIdStr);
            const int time = std::stoi(timeStr);
            if (event == "start") {
                if (!stack.empty()) {
                    result[stack.back()] += time - prevTime;
                }
                stack.push_back(funcId);
                prevTime = time;
            } else {
                result[stack.back()] += time - prevTime + 1;
                stack.pop_back();
                prevTime = time + 1;
            }
        }
        return result;
    }
};

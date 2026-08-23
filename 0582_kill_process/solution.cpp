// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> killProcess(std::vector<int>& pid, std::vector<int>& ppid, int kill) {
        std::unordered_map<int, std::vector<int>> children;
        for (size_t i = 0; i < pid.size(); ++i) {
            children[ppid[i]].push_back(pid[i]);
        }

        std::vector<int> result;
        std::queue<int> queue;
        queue.push(kill);
        while (!queue.empty()) {
            int process = queue.front();
            queue.pop();
            result.push_back(process);
            for (int child : children[process]) {
                queue.push(child);
            }
        }
        return result;
    }
};

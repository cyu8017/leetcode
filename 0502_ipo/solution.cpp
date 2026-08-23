// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

#include <algorithm>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int findMaximizedCapital(int k, int w, std::vector<int>& profits, std::vector<int>& capital) {
        std::vector<std::pair<int, int>> projects;
        projects.reserve(capital.size());
        for (size_t index = 0; index < capital.size(); ++index) {
            projects.emplace_back(capital[index], profits[index]);
        }
        std::sort(projects.begin(), projects.end());

        std::priority_queue<int> available;
        size_t index = 0;
        for (int round = 0; round < k; ++round) {
            while (index < projects.size() && projects[index].first <= w) {
                available.push(projects[index].second);
                ++index;
            }
            if (available.empty()) {
                break;
            }
            w += available.top();
            available.pop();
        }
        return w;
    }
};

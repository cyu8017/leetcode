// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

#include <vector>

class Solution {
public:
    std::vector<int> simulationResult(std::vector<int>& windows, std::vector<int>& queries) {
        int n = (int)windows.size();
        std::vector<char> s(n + 1, 0);
        std::vector<int> ans;
        for (int i = (int)queries.size() - 1; i >= 0; i--) {
            int q = queries[i];
            if (!s[q]) {
                s[q] = 1;
                ans.push_back(q);
            }
        }
        for (int w : windows) {
            if (!s[w]) ans.push_back(w);
        }
        return ans;
    }
};

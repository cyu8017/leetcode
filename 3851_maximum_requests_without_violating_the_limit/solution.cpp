// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxRequests(std::vector<std::vector<int>>& requests, int k, int window) {
        std::unordered_map<int, std::vector<int>> g;
        for (auto& r : requests) g[r[0]].push_back(r[1]);
        int ans = (int)requests.size();
        for (auto& [_, ts] : g) {
            std::sort(ts.begin(), ts.end());
            std::vector<int> kept;
            for (int t : ts) {
                while (!kept.empty() && t - kept.front() > window) kept.erase(kept.begin());
                if ((int)kept.size() < k) kept.push_back(t);
                else ans--;
            }
        }
        return ans;
    }
};

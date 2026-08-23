// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxStudentsOnBench(std::vector<std::vector<int>>& students) {
        std::unordered_map<int, std::unordered_set<int>> bench;
        for (auto& s : students) {
            int sid = s[0], b = s[1];
            bench[b].insert(sid);
        }
        int ans = 0;
        for (auto& [_, set] : bench) {
            if ((int)set.size() > ans) ans = (int)set.size();
        }
        return ans;
    }
};

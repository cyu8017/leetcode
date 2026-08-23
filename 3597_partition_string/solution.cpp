// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> partitionString(std::string s) {
        std::unordered_set<std::string> vis;
        std::vector<std::string> ans;
        std::string t;
        for (char c : s) {
            t += c;
            if (!vis.count(t)) {
                vis.insert(t);
                ans.push_back(t);
                t.clear();
            }
        }
        return ans;
    }
};

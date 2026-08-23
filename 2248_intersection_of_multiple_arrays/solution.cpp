// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    std::vector<int> intersection(std::vector<std::vector<int>>& nums) {
        std::unordered_map<int, int> freq;
        for (auto& arr : nums) {
            std::unordered_set<int> seen;
            for (int x : arr) {
                if (seen.insert(x).second) freq[x]++;
            }
        }
        std::vector<int> ans;
        for (auto& [x, c] : freq) if (c == (int)nums.size()) ans.push_back(x);
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};

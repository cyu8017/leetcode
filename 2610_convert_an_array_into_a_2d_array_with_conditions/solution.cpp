// LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findMatrix(std::vector<int>& nums) {
        std::unordered_map<int, int> freq;
        std::vector<std::vector<int>> ans;
        for (int x : nums) {
            int f = freq[x];
            if (f == (int)ans.size()) ans.push_back({});
            ans[f].push_back(x);
            freq[x]++;
        }
        return ans;
    }
};

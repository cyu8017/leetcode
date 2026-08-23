// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> arrayChange(std::vector<int>& nums, std::vector<std::vector<int>>& operations) {
        std::unordered_map<int, int> pos;
        for (int i = 0; i < (int)nums.size(); ++i) pos[nums[i]] = i;
        for (auto& op : operations) {
            int i = pos[op[0]];
            nums[i] = op[1];
            pos.erase(op[0]);
            pos[op[1]] = i;
        }
        return nums;
    }
};

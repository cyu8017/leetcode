// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

#include <vector>

class Solution {
public:
    std::vector<int> occurrencesOfElement(std::vector<int>& nums, std::vector<int>& queries, int x) {
        std::vector<int> ids;
        for (int i = 0; i < (int)nums.size(); i++) if (nums[i] == x) ids.push_back(i);
        std::vector<int> ans;
        for (int i : queries) {
            if (i - 1 < (int)ids.size()) ans.push_back(ids[i - 1]);
            else ans.push_back(-1);
        }
        return ans;
    }
};

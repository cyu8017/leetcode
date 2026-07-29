// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> rearrangeArray(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size(), mid = (n + 1) / 2;
        std::vector<int> small(nums.begin(), nums.begin() + mid);
        std::vector<int> large(nums.begin() + mid, nums.end());
        std::vector<int> ans;
        int i = 0, j = 0;
        while (i < (int)small.size() || j < (int)large.size()) {
            if (i < (int)small.size()) ans.push_back(small[i++]);
            if (j < (int)large.size()) ans.push_back(large[j++]);
        }
        return ans;
    }
};

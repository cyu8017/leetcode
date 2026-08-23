// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> relocateMarbles(std::vector<int>& nums, std::vector<int>& moveFrom, std::vector<int>& moveTo) {
        std::unordered_set<int> pos(nums.begin(), nums.end());
        for (int i = 0; i < (int)moveFrom.size(); i++) {
            pos.erase(moveFrom[i]);
            pos.insert(moveTo[i]);
        }
        std::vector<int> ans(pos.begin(), pos.end());
        std::sort(ans.begin(), ans.end());
        return ans;
    }
};

// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    std::vector<int> advantageCount(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::deque<int> sorted1(nums1.begin(), nums1.end());
        std::sort(sorted1.begin(), sorted1.end());
        std::vector<int> ans(nums1.size());
        std::vector<std::pair<int, int>> indexed;
        for (int i = 0; i < static_cast<int>(nums2.size()); ++i) {
            indexed.emplace_back(nums2[i], i);
        }
        std::sort(indexed.begin(), indexed.end(), std::greater<>());
        for (auto [val, i] : indexed) {
            if (sorted1.back() > val) {
                ans[i] = sorted1.back();
                sorted1.pop_back();
            } else {
                ans[i] = sorted1.front();
                sorted1.pop_front();
            }
        }
        return ans;
    }
};

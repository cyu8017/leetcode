// LeetCode 0373 - Find K Pairs with Smallest Sums
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> kSmallestPairs(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        if (nums1.empty() || nums2.empty() || k == 0) {
            return {};
        }

        using Entry = std::tuple<int, int, int>;
        auto compare = [](const Entry& left, const Entry& right) {
            return std::get<0>(left) > std::get<0>(right);
        };

        std::priority_queue<Entry, std::vector<Entry>, decltype(compare)> heap(compare);
        std::vector<std::vector<int>> result;

        for (int index = 0; index < static_cast<int>(nums1.size()) && index < k; ++index) {
            heap.push({nums1[index] + nums2[0], index, 0});
        }

        while (!heap.empty() && static_cast<int>(result.size()) < k) {
            auto [total, index1, index2] = heap.top();
            (void)total;
            heap.pop();
            result.push_back({nums1[index1], nums2[index2]});
            if (index2 + 1 < static_cast<int>(nums2.size())) {
                heap.push({nums1[index1] + nums2[index2 + 1], index1, index2 + 1});
            }
        }

        return result;
    }
};

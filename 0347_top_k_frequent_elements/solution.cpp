// LeetCode 0347 - Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        for (int num : nums) {
            counts[num] += 1;
        }

        std::vector<std::vector<int>> buckets(nums.size() + 1);
        for (const auto& entry : counts) {
            buckets[entry.second].push_back(entry.first);
        }

        std::vector<int> result;
        for (int index = static_cast<int>(buckets.size()) - 1; index >= 0; --index) {
            for (int value : buckets[index]) {
                result.push_back(value);
                if (static_cast<int>(result.size()) == k) {
                    return result;
                }
            }
        }

        return result;
    }
};

// LeetCode 1985 - Find the Kth Largest Integer in the Array
#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string kthLargestNumber(std::vector<std::string>& nums, int k) {
        std::sort(nums.begin(), nums.end(), [](const std::string& a, const std::string& b) {
            if (a.size() != b.size()) return a.size() > b.size();
            return a > b;
        });
        return nums[k - 1];
    }
};

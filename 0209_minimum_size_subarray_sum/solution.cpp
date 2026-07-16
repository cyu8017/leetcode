// LeetCode 0209 - Minimum Size Subarray Sum
#include <algorithm>
#include <climits>
#include <vector>
class Solution { public: int minSubArrayLen(int target, std::vector<int>& nums) { int left = 0, total = 0, best = INT_MAX; for (int right = 0; right < static_cast<int>(nums.size()); ++right) { total += nums[right]; while (total >= target) { best = std::min(best, right - left + 1); total -= nums[left++]; } } return best == INT_MAX ? 0 : best; } };

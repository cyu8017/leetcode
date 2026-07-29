#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums, int limit) {
        std::deque<int> low, high;
        int left = 0, answer = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            while (!low.empty() && nums[low.back()] > nums[right]) low.pop_back();
            while (!high.empty() && nums[high.back()] < nums[right]) high.pop_back();
            low.push_back(right);
            high.push_back(right);
            while (nums[high.front()] - nums[low.front()] > limit) {
                ++left;
                if (low.front() < left) low.pop_front();
                if (high.front() < left) high.pop_front();
            }
            answer = std::max(answer, right - left + 1);
        }
        return answer;
    }
};

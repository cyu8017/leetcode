#include <vector>

class Solution {
public:
    std::vector<int> shuffle(std::vector<int>& nums, int n) {
        std::vector<int> answer;
        for (int i = 0; i < n; ++i) {
            answer.push_back(nums[i]);
            answer.push_back(nums[i + n]);
        }
        return answer;
    }
};

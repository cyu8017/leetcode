#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> minSubsequence(std::vector<int>& nums) {
        std::sort(nums.rbegin(), nums.rend());
        int total = std::accumulate(nums.begin(), nums.end(), 0);
        std::vector<int> answer;
        int chosen = 0;
        for (int value : nums) {
            answer.push_back(value);
            chosen += value;
            if (chosen > total - chosen) return answer;
        }
        return answer;
    }
};

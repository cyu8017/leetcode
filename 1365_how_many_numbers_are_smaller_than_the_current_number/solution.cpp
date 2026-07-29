#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> smallerNumbersThanCurrent(std::vector<int>& nums) {
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        std::vector<int> answer;
        for (int x : nums)
            answer.push_back((int)(std::lower_bound(sorted.begin(), sorted.end(), x) - sorted.begin()));
        return answer;
    }
};

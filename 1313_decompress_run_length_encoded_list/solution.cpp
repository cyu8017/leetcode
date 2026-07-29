#include <vector>

class Solution {
public:
    std::vector<int> decompressRLElist(std::vector<int>& nums) {
        std::vector<int> answer;
        for (int i = 0; i < (int)nums.size(); i += 2)
            answer.insert(answer.end(), nums[i], nums[i + 1]);
        return answer;
    }
};

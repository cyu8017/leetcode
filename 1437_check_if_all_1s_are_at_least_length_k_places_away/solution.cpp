#include <vector>

class Solution {
public:
    bool kLengthApart(std::vector<int>& nums, int k) {
        int previous = -k - 1;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i]) {
                if (i - previous <= k) return false;
                previous = i;
            }
        }
        return true;
    }
};

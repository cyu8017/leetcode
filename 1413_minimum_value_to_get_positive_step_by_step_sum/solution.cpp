#include <algorithm>
#include <vector>

class Solution {
public:
    int minStartValue(std::vector<int>& nums) {
        int prefix = 0, lowest = 0;
        for (int value : nums) {
            prefix += value;
            lowest = std::min(lowest, prefix);
        }
        return 1 - lowest;
    }
};

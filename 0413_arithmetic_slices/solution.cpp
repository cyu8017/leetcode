// LeetCode 0413 - Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

#include <vector>

using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) {
            return 0;
        }

        int total = 0;
        int current = 0;

        for (size_t index = 2; index < nums.size(); ++index) {
            if (nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]) {
                current += 1;
                total += current;
            } else {
                current = 0;
            }
        }

        return total;
    }
};

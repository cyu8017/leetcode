// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

#include <vector>

class Solution {
public:
    std::vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        int jumbo = tomatoSlices / 2 - cheeseSlices;
        int small = cheeseSlices - jumbo;
        if (tomatoSlices % 2 == 0 && jumbo >= 0 && small >= 0) {
            return {jumbo, small};
        }
        return {};
    }
};

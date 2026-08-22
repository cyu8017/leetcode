// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

#include <stdlib.h>

int* numOfBurgers(int tomatoSlices, int cheeseSlices, int* returnSize) {
    *returnSize = 0;
    if (tomatoSlices % 2) return NULL;
    int jumbo = tomatoSlices / 2 - cheeseSlices;
    int small = cheeseSlices - jumbo;
    if (jumbo < 0 || small < 0) return NULL;
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = jumbo;
    ans[1] = small;
    *returnSize = 2;
    return ans;
}

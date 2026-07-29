// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

#include <stdlib.h>
#include <string.h>

int* distributeCandies(int candies, int num_people, int* returnSize) {
    int* ans = (int*)calloc((size_t)num_people, sizeof(int));
    int give = 1, i = 0;
    while (candies > 0) {
        int take = give < candies ? give : candies;
        ans[i] += take;
        candies -= take;
        give++;
        i = (i + 1) % num_people;
    }
    *returnSize = num_people;
    return ans;
}

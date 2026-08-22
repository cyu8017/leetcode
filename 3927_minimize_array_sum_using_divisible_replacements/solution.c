// LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
// https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

long long minArraySum(int* nums, int numsSize) {
    int maximum = 0;
    bool present[100001];
    memset(present, 0, sizeof(present));
    for (int i = 0; i < numsSize; i++) {
        present[nums[i]] = true;
        if (nums[i] > maximum) maximum = nums[i];
    }
    int* best = calloc((size_t)(maximum + 1), sizeof(int));
    for (int divisor = 1; divisor <= maximum; divisor++) {
        if (!present[divisor]) continue;
        for (int multiple = divisor; multiple <= maximum; multiple += divisor) {
            if (best[multiple] == 0) best[multiple] = divisor;
        }
    }
    long long answer = 0;
    for (int i = 0; i < numsSize; i++) answer += best[nums[i]];
    free(best);
    return answer;
}

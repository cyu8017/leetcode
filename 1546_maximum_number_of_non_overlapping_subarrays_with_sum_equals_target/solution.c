// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

#include <stdlib.h>

int maxNonOverlapping(int* nums, int numsSize, int target) {
    int* seen = (int*)malloc((size_t)(numsSize + 1) * sizeof(int));
    int seenSize = 1;
    seen[0] = 0;
    int prefix = 0, answer = 0;
    for (int i = 0; i < numsSize; i++) {
        prefix += nums[i];
        int found = 0;
        for (int j = 0; j < seenSize; j++) {
            if (seen[j] == prefix - target) { found = 1; break; }
        }
        if (found) {
            answer++;
            prefix = 0;
            seenSize = 1;
            seen[0] = 0;
        } else {
            seen[seenSize++] = prefix;
        }
    }
    free(seen);
    return answer;
}

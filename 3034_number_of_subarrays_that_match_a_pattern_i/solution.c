// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

static int fcmp(int a, int b) {
    if (a == b) return 0;
    return a < b ? 1 : -1;
}

int countMatchingSubarrays(int* nums, int numsSize, int* pattern, int patternSize) {
    int ans = 0;
    for (int i = 0; i < numsSize - patternSize; i++) {
        int ok = 1;
        for (int k = 0; k < patternSize && ok; k++) {
            if (fcmp(nums[i + k], nums[i + k + 1]) != pattern[k]) ok = 0;
        }
        ans += ok;
    }
    return ans;
}

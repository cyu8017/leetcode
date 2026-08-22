// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

#include <stdlib.h>
#include <string.h>

static void reverseRange(char* nums, int l, int r) {
    while (l < r) {
        char t = nums[l];
        nums[l] = nums[r];
        nums[r] = t;
        l++;
        r--;
    }
}

static int nextPermutationHalf(char* nums, int half) {
    int i = half - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) i--;
    if (i < 0) return 0;
    int j = half - 1;
    while (nums[j] <= nums[i]) j--;
    char t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
    reverseRange(nums, i + 1, half - 1);
    return 1;
}

char* nextPalindrome(char* num) {
    int n = (int)strlen(num);
    char* nums = (char*)malloc((size_t)n + 1);
    strcpy(nums, num);
    if (!nextPermutationHalf(nums, n / 2)) {
        free(nums);
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    for (int i = 0; i < n / 2; i++) nums[n - i - 1] = nums[i];
    return nums;
}

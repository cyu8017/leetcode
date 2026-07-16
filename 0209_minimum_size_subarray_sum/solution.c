// LeetCode 0209 - Minimum Size Subarray Sum
#include <limits.h>
int minSubArrayLen(int target, int* nums, int numsSize) { int left = 0, total = 0, best = INT_MAX; for (int right = 0; right < numsSize; ++right) { total += nums[right]; while (total >= target) { int length = right - left + 1; if (length < best) best = length; total -= nums[left++]; } } return best == INT_MAX ? 0 : best; }

// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

#include <stdlib.h>
#include <string.h>

long long maximumSubarraySum(int* nums, int numsSize, int k) {
    /* nums[i] up to 1e5 */
    int* cnt = (int*)calloc(100001, sizeof(int));
    int distinct = 0;
    long long sum = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        sum += x;
        if (cnt[x]++ == 0) distinct++;
        if (i >= k) {
            int y = nums[i - k];
            sum -= y;
            if (--cnt[y] == 0) distinct--;
        }
        if (i >= k - 1 && distinct == k && sum > ans) ans = sum;
    }
    free(cnt);
    return ans;
}

// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

#include <stdlib.h>

long long countSubarrays(int* nums, int numsSize, long long k) {
    long long ans = 0;
    int* q1 = (int*)malloc((size_t)numsSize * sizeof(int));
    int* q2 = (int*)malloc((size_t)numsSize * sizeof(int));
    int h1 = 0, t1 = 0, h2 = 0, t2 = 0;
    int l = 0;
    for (int r = 0; r < numsSize; r++) {
        int x = nums[r];
        while (t1 > h1 && nums[q1[t1 - 1]] <= x) t1--;
        while (t2 > h2 && nums[q2[t2 - 1]] >= x) t2--;
        q1[t1++] = r;
        q2[t2++] = r;
        while (l < r && (long long)(nums[q1[h1]] - nums[q2[h2]]) * (r - l + 1) > k) {
            l++;
            if (q1[h1] < l) h1++;
            if (q2[h2] < l) h2++;
        }
        ans += r - l + 1;
    }
    free(q1); free(q2);
    return ans;
}

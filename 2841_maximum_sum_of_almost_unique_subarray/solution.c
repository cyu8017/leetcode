// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

#include <stdlib.h>

typedef struct { int key, cnt, used; } E;

long long maxSum(int* nums, int numsSize, int m, int k) {
    int htsz = 4096;
    E* ht = (E*)calloc(htsz, sizeof(E));
    int distinct = 0;
    long long sum = 0, ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        unsigned h = ((unsigned)v * 2654435761u) % htsz;
        while (ht[h].used && ht[h].key != v) h = (h + 1) % htsz;
        if (!ht[h].used) { ht[h].used = 1; ht[h].key = v; ht[h].cnt = 0; }
        if (ht[h].cnt == 0) distinct++;
        ht[h].cnt++;
        sum += v;
        if (i >= k) {
            int out = nums[i - k];
            sum -= out;
            unsigned ho = ((unsigned)out * 2654435761u) % htsz;
            while (ht[ho].used && ht[ho].key != out) ho = (ho + 1) % htsz;
            ht[ho].cnt--;
            if (ht[ho].cnt == 0) distinct--;
        }
        if (i >= k - 1 && distinct >= m && sum > ans) ans = sum;
    }
    free(ht);
    return ans;
}

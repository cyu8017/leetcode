// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

#include <stdlib.h>
#include <string.h>

int minimumBuckets(char* hamsters) {
    int n = (int)strlen(hamsters);
    char* b = (char*)malloc((size_t)n + 1);
    strcpy(b, hamsters);
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (b[i] != 'H') continue;
        if (i > 0 && b[i - 1] == 'B') continue;
        if (i + 1 < n && b[i + 1] == '.') { b[i + 1] = 'B'; ans++; }
        else if (i > 0 && b[i - 1] == '.') { b[i - 1] = 'B'; ans++; }
        else { free(b); return -1; }
    }
    free(b);
    return ans;
}

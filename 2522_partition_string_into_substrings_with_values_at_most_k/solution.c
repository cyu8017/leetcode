// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

#include <string.h>

int minimumPartition(char* s, int k) {
    int ans = 1;
    long long cur = 0;
    for (int i = 0; s[i]; i++) {
        int d = s[i] - '0';
        if (d > k) return -1;
        long long nxt = cur * 10 + d;
        if (nxt > k) { ans++; cur = d; }
        else cur = nxt;
    }
    return ans;
}

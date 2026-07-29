// LeetCode 1461 - Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool hasAllCodes(char* s, int k) {
    int n = (int)strlen(s);
    if (n < k) return false;
    int need = 1 << k;
    bool* seen = (bool*)calloc(need, sizeof(bool));
    int count = 0, mask = 0, all = need - 1;
    for (int i = 0; i < n; i++) {
        mask = ((mask << 1) | (s[i] - '0')) & all;
        if (i >= k - 1 && !seen[mask]) { seen[mask] = true; count++; }
    }
    free(seen);
    return count == need;
}

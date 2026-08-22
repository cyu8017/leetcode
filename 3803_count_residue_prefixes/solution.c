// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

#include <string.h>
#include <stdbool.h>

int residuePrefixes(char* s) {
    bool seen[256] = {false};
    int distinct = 0, ans = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        unsigned char c = (unsigned char)s[i];
        if (!seen[c]) { seen[c] = true; distinct++; }
        int idx = i + 1;
        if (distinct == idx % 3) ans++;
    }
    return ans;
}

// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool maxSubstringLength(char* s, int k) {
    int n = (int)strlen(s);
    int first[26], last[26];
    for (int i = 0; i < 26; i++) { first[i] = n; last[i] = -1; }
    for (int i = 0; i < n; i++) {
        int ci = s[i] - 'a';
        if (first[ci] == n) first[ci] = i;
        last[ci] = i;
    }
    int segsL[64], segsR[64], sc = 0;
    for (int c = 0; c < 26; c++) {
        if (last[c] == -1) continue;
        int l = first[c], r = last[c];
        for (int i = l; i <= r; i++) {
            int ci = s[i] - 'a';
            if (first[ci] < l) { l = first[ci]; i = l - 1; continue; }
            if (last[ci] > r) r = last[ci];
        }
        if (!(l == 0 && r == n - 1)) {
            segsL[sc] = l; segsR[sc] = r; sc++;
        }
    }
    int arrL[64], arrR[64], ac = 0;
    for (int i = 0; i < sc; i++) {
        int dup = 0;
        for (int j = 0; j < ac; j++) {
            if (arrL[j] == segsL[i] && arrR[j] == segsR[i]) { dup = 1; break; }
        }
        if (!dup) { arrL[ac] = segsL[i]; arrR[ac] = segsR[i]; ac++; }
    }
    for (int i = 0; i < ac; i++) {
        for (int j = i + 1; j < ac; j++) {
            if (arrR[j] < arrR[i]) {
                int tl = arrL[i], tr = arrR[i];
                arrL[i] = arrL[j]; arrR[i] = arrR[j];
                arrL[j] = tl; arrR[j] = tr;
            }
        }
    }
    int cnt = 0, end = -1;
    for (int i = 0; i < ac; i++) {
        if (arrL[i] > end) { cnt++; end = arrR[i]; }
    }
    return cnt >= k;
}

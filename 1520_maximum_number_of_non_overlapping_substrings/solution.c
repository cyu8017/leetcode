// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

#include <stdlib.h>
#include <string.h>

static int cmpInterval(const void* a, const void* b) {
    const int* x = (const int*)a;
    const int* y = (const int*)b;
    if (x[0] != y[0]) return x[0] - y[0];
    return x[1] - y[1];
}

static int cmpLen(const void* a, const void* b) {
    const char* sa = *(const char* const*)a;
    const char* sb = *(const char* const*)b;
    int la = (int)strlen(sa), lb = (int)strlen(sb);
    if (la != lb) return la - lb;
    return strcmp(sa, sb);
}

char** maxNumOfSubstrings(char* s, int* returnSize) {
    int n = (int)strlen(s);
    int first[26], last[26];
    for (int i = 0; i < 26; i++) first[i] = last[i] = -1;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (first[c] < 0) first[c] = i;
        last[c] = i;
    }
    int intervals[26][2];
    int ic = 0;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (first[c] != i) continue;
        int end = last[c];
        int j = i;
        int valid = 1;
        while (j <= end) {
            int cj = s[j] - 'a';
            if (first[cj] < i) { valid = 0; break; }
            if (last[cj] > end) end = last[cj];
            j++;
        }
        if (valid) {
            intervals[ic][0] = end;
            intervals[ic][1] = i;
            ic++;
        }
    }
    qsort(intervals, (size_t)ic, sizeof(intervals[0]), cmpInterval);
    char** answer = (char**)malloc((size_t)ic * sizeof(char*));
    int ac = 0, previous_end = -1;
    for (int t = 0; t < ic; t++) {
        int end = intervals[t][0], start = intervals[t][1];
        if (start > previous_end) {
            int len = end - start + 1;
            char* part = (char*)malloc((size_t)len + 1);
            memcpy(part, s + start, (size_t)len);
            part[len] = '\0';
            answer[ac++] = part;
            previous_end = end;
        }
    }
    qsort(answer, (size_t)ac, sizeof(char*), cmpLen);
    *returnSize = ac;
    return answer;
}

// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

#include <stdlib.h>
#include <string.h>

static void build_lps(int* lps, int sl, const char* pattern) {
    int l = 0; lps[0] = 0; int i = 1;
    while (i < sl) {
        if (pattern[i] == pattern[l]) { l++; lps[i] = l; i++; }
        else if (l != 0) l = lps[l - 1];
        else { lps[i] = l; i++; }
    }
}

static void kmp_find(const char* s, int s_len, const char* pat, int pat_l, int* lps, int** index, int* sz, int* cap) {
    int i = 0, j = 0;
    while (s_len - i >= pat_l - j) {
        if (s[i] == pat[j]) { i++; j++; }
        if (j == pat_l) {
            if (*sz == *cap) { *cap = *cap ? *cap * 2 : 8; *index = (int*)realloc(*index, (size_t)(*cap) * sizeof(int)); }
            (*index)[(*sz)++] = i - pat_l;
            j = lps[j - 1];
        } else if (i < s_len && s[i] != pat[j]) {
            if (j != 0) j = lps[j - 1];
            else i++;
        } else if (i >= s_len) break;
    }
}

int* beautifulIndices(char* s, char* a, char* b, int k, int* returnSize) {
    int s_len = (int)strlen(s), a_len = (int)strlen(a), b_len = (int)strlen(b);
    int* lps_a = (int*)malloc((size_t)a_len * sizeof(int));
    int* lps_b = (int*)malloc((size_t)b_len * sizeof(int));
    build_lps(lps_a, a_len, a);
    build_lps(lps_b, b_len, b);
    int *a_index = NULL, *b_index = NULL, asz = 0, bsz = 0, acap = 0, bcap = 0;
    kmp_find(s, s_len, a, a_len, lps_a, &a_index, &asz, &acap);
    kmp_find(s, s_len, b, b_len, lps_b, &b_index, &bsz, &bcap);
    int* final = (int*)malloc((size_t)(asz + 1) * sizeof(int));
    int fn = 0, i = 0, j = 0;
    while (i < asz && j < bsz) {
        if (a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]) { final[fn++] = a_index[i]; i++; }
        else if (a_index[i] - k > b_index[j]) j++;
        else i++;
    }
    free(lps_a); free(lps_b); free(a_index); free(b_index);
    *returnSize = fn;
    return final;
}

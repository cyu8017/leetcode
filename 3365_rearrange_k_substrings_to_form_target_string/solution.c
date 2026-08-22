// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPossibleToRearrange(char* s, char* t, int k) {
    int n = (int)strlen(s), sz = n / k;
    /* simple: sort chunks of s and t and compare */
    char** a = (char**)malloc(k * sizeof(char*));
    char** b = (char**)malloc(k * sizeof(char*));
    for (int i = 0; i < k; i++) {
        a[i] = (char*)malloc(sz + 1); memcpy(a[i], s + i * sz, sz); a[i][sz] = 0;
        b[i] = (char*)malloc(sz + 1); memcpy(b[i], t + i * sz, sz); b[i][sz] = 0;
    }
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) {
        if (strcmp(a[i], a[j]) > 0) { char* tmp = a[i]; a[i] = a[j]; a[j] = tmp; }
        if (strcmp(b[i], b[j]) > 0) { char* tmp = b[i]; b[i] = b[j]; b[j] = tmp; }
    }
    int ok = 1;
    for (int i = 0; i < k; i++) if (strcmp(a[i], b[i]) != 0) { ok = 0; break; }
    for (int i = 0; i < k; i++) { free(a[i]); free(b[i]); }
    free(a); free(b);
    return ok;
}

// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

#define _POSIX_C_SOURCE 200809L

#include <stdlib.h>
#include <string.h>

static void reverseCopy(char* dest, const char* src) {
    int n = (int)strlen(src);
    for (int i = 0; i < n; i++) {
        dest[i] = src[n - 1 - i];
    }
    dest[n] = '\0';
}

char* splitLoopedString(char** strs, int strsSize) {
    char** bestForms = (char**)malloc((size_t)strsSize * sizeof(char*));
    for (int i = 0; i < strsSize; i++) {
        int len = (int)strlen(strs[i]);
        char* rev = (char*)malloc((size_t)len + 1);
        reverseCopy(rev, strs[i]);
        bestForms[i] = strcmp(strs[i], rev) >= 0 ? strdup(strs[i]) : rev;
        if (bestForms[i] != rev) {
            free(rev);
        }
    }

    char* answer = strdup("");
    for (int i = 0; i < strsSize; i++) {
        int midLen = 0;
        for (int j = 0; j < strsSize; j++) {
            if (j != i) {
                midLen += (int)strlen(bestForms[j]);
            }
        }
        char* mid = (char*)malloc((size_t)midLen + 1);
        mid[0] = '\0';
        for (int j = i + 1; j < strsSize; j++) {
            strcat(mid, bestForms[j]);
        }
        for (int j = 0; j < i; j++) {
            strcat(mid, bestForms[j]);
        }

        char* candidates[2];
        int len = (int)strlen(strs[i]);
        candidates[0] = strdup(strs[i]);
        candidates[1] = (char*)malloc((size_t)len + 1);
        reverseCopy(candidates[1], strs[i]);

        for (int c = 0; c < 2; c++) {
            char* candidate = candidates[c];
            for (int cut = 0; cut < len; cut++) {
                char* formed = (char*)malloc((size_t)len + midLen + 1);
                strcpy(formed, candidate + cut);
                strcat(formed, mid);
                strncat(formed, candidate, (size_t)cut);
                if (strcmp(formed, answer) > 0) {
                    free(answer);
                    answer = formed;
                } else {
                    free(formed);
                }
            }
            free(candidate);
        }
        free(mid);
    }

    for (int i = 0; i < strsSize; i++) {
        free(bestForms[i]);
    }
    free(bestForms);
    return answer;
}

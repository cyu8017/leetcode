// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char** shortestSubstrings(char** arr, int arrSize, int* returnSize) {
    char** ans = (char**)malloc((size_t)arrSize * sizeof(char*));
    for (int i = 0; i < arrSize; i++) {
        ans[i] = (char*)malloc(1); ans[i][0] = '\0';
        int m = (int)strlen(arr[i]);
        for (int j = 1; j <= m && ans[i][0] == '\0'; j++) {
            for (int l = 0; l <= m - j; l++) {
                char* sub = (char*)malloc((size_t)j + 1);
                memcpy(sub, arr[i] + l, (size_t)j); sub[j] = '\0';
                if (ans[i][0] == '\0' || strcmp(ans[i], sub) > 0) {
                    bool ok = true;
                    for (int k = 0; k < arrSize; k++) {
                        if (k != i && strstr(arr[k], sub)) { ok = false; break; }
                    }
                    if (ok) { free(ans[i]); ans[i] = sub; }
                    else free(sub);
                } else free(sub);
            }
        }
    }
    *returnSize = arrSize;
    return ans;
}

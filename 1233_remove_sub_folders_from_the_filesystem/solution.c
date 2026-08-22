// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

#include <stdlib.h>
#include <string.h>

static int cmpStr(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

char** removeSubfolders(char** folder, int folderSize, int* returnSize) {
    qsort(folder, (size_t)folderSize, sizeof(char*), cmpStr);
    char** answer = (char**)malloc((size_t)folderSize * sizeof(char*));
    int count = 0;
    for (int i = 0; i < folderSize; i++) {
        if (count == 0) {
            answer[count++] = folder[i];
            continue;
        }
        char* prev = answer[count - 1];
        int prevLen = (int)strlen(prev);
        if (strncmp(folder[i], prev, (size_t)prevLen) == 0 && folder[i][prevLen] == '/') continue;
        answer[count++] = folder[i];
    }
    *returnSize = count;
    return answer;
}

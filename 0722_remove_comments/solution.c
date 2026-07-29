// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeComments(char** source, int sourceSize, int* returnSize) {
    char** result = (char**)malloc((size_t)sourceSize * sizeof(char*));
    int rsize = 0;
    char* buffer = (char*)malloc(10000);
    int bsize = 0;
    bool inBlock = false;

    for (int lineIdx = 0; lineIdx < sourceSize; lineIdx++) {
        char* line = source[lineIdx];
        int i = 0;
        int len = (int)strlen(line);
        while (i < len) {
            if (inBlock) {
                if (i + 1 < len && line[i] == '*' && line[i + 1] == '/') {
                    inBlock = false;
                    i += 2;
                } else {
                    i++;
                }
            } else if (i + 1 < len && line[i] == '/' && line[i + 1] == '*') {
                inBlock = true;
                i += 2;
            } else if (i + 1 < len && line[i] == '/' && line[i + 1] == '/') {
                break;
            } else {
                buffer[bsize++] = line[i++];
            }
        }
        if (!inBlock && bsize > 0) {
            buffer[bsize] = '\0';
            result[rsize] = (char*)malloc((size_t)bsize + 1);
            strcpy(result[rsize], buffer);
            rsize++;
            bsize = 0;
        }
    }

    free(buffer);
    *returnSize = rsize;
    return result;
}

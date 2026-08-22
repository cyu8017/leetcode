// LeetCode 0388 - Longest Absolute File Path
// https://leetcode.com/problems/longest-absolute-file-path/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int lengthLongestPath(char* input) {
    int* stack = NULL;
    int stackSize = 0;
    int stackCapacity = 0;
    int maxLength = 0;
    int index = 0;
    int length = (int)strlen(input);

    while (index < length) {
        int end = index;
        while (end < length && input[end] != '\n') {
            end += 1;
        }

        int depth = 0;
        while (index + depth < end && input[index + depth] == '\t') {
            depth += 1;
        }

        int nameStart = index + depth;
        int nameLength = end - nameStart;
        bool isFile = false;
        for (int position = nameStart; position < end; position++) {
            if (input[position] == '.') {
                isFile = true;
                break;
            }
        }

        while (stackSize > depth) {
            stackSize -= 1;
        }

        if (isFile) {
            int prefix = stackSize > 0 ? stack[stackSize - 1] : 0;
            int total = prefix + nameLength;
            if (total > maxLength) {
                maxLength = total;
            }
        } else {
            int prefix = stackSize > 0 ? stack[stackSize - 1] : 0;
            if (stackSize >= stackCapacity) {
                stackCapacity = stackCapacity == 0 ? 4 : stackCapacity * 2;
                stack = (int*)realloc(stack, (size_t)stackCapacity * sizeof(int));
            }
            stack[stackSize++] = prefix + nameLength + 1;
        }

        index = end + 1;
    }

    free(stack);
    return maxLength;
}

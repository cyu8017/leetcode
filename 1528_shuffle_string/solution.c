// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

#include <stdlib.h>
#include <string.h>

char* restoreString(char* s, int* indices, int indicesSize) {
    char* answer = (char*)malloc((size_t)indicesSize + 1);
    answer[indicesSize] = '\0';
    for (int i = 0; i < indicesSize; i++) {
        answer[indices[i]] = s[i];
    }
    return answer;
}

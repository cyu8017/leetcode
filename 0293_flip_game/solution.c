// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

#include <stdlib.h>
#include <string.h>

char** generatePossibleNextMoves(char* currentState, int* returnSize) {
    *returnSize = 0;
    int length = (int)strlen(currentState);
    if (length < 2) {
        return NULL;
    }

    char** result = NULL;
    int capacity = 0;

    for (int index = 0; index + 1 < length; index++) {
        if (currentState[index] == '+' && currentState[index + 1] == '+') {
            if (*returnSize == capacity) {
                capacity = capacity == 0 ? 4 : capacity * 2;
                result = (char**)realloc(result, (size_t)capacity * sizeof(char*));
            }
            char* nextState = strdup(currentState);
            nextState[index] = '-';
            nextState[index + 1] = '-';
            result[*returnSize] = nextState;
            (*returnSize)++;
        }
    }

    return result;
}

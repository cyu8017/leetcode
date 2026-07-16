// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

static char* shrink(const char* source) {
    int length = (int)strlen(source);
    char* buffer = (char*)malloc((size_t)length + 1);
    strcpy(buffer, source);
    int changed = 1;
    while (changed) {
        changed = 0;
        length = (int)strlen(buffer);
        int index = 0;
        while (index < length) {
            int end = index;
            while (end < length && buffer[end] == buffer[index]) {
                end++;
            }
            if (end - index >= 3) {
                memmove(buffer + index, buffer + end, (size_t)length - end + 1);
                changed = 1;
                break;
            }
            index = end;
        }
    }
    return buffer;
}

static int dfs(char* board, char* hand, char** memoKeys, int* memoValues, int* memoSize) {
    char key[256];
    snprintf(key, sizeof(key), "%s#%s", board, hand);
    for (int index = 0; index < *memoSize; index++) {
        if (strcmp(memoKeys[index], key) == 0) {
            return memoValues[index];
        }
    }
    char* shrunk = shrink(board);
    strcpy(board, shrunk);
    free(shrunk);
    if (board[0] == '\0') {
        memoKeys[*memoSize] = strdup(key);
        memoValues[*memoSize] = 0;
        (*memoSize)++;
        return 0;
    }
    int best = INT_MAX;
    int boardLength = (int)strlen(board);
    int handLength = (int)strlen(hand);
    for (int insert = 0; insert <= boardLength; insert++) {
        for (int pick = 0; pick < handLength; pick++) {
            char color = hand[pick];
            if (insert < boardLength && board[insert] == color) {
                // allowed
            } else if (insert > 0 && board[insert - 1] == color) {
                // allowed
            } else {
                continue;
            }
            char nextBoard[128];
            strncpy(nextBoard, board, (size_t)insert);
            nextBoard[insert] = color;
            strcpy(nextBoard + insert + 1, board + insert);
            char* shrunkNext = shrink(nextBoard);
            if (strcmp(shrunkNext, board) == 0) {
                free(shrunkNext);
                continue;
            }
            char nextHand[32];
            strncpy(nextHand, hand, (size_t)pick);
            nextHand[pick] = '\0';
            strcat(nextHand, hand + pick + 1);
            int steps = dfs(shrunkNext, nextHand, memoKeys, memoValues, memoSize);
            free(shrunkNext);
            if (steps != INT_MAX && steps + 1 < best) {
                best = steps + 1;
            }
        }
    }
    memoKeys[*memoSize] = strdup(key);
    memoValues[*memoSize] = best;
    (*memoSize)++;
    return best;
}

int findMinStep(char* board, char* hand) {
    char** memoKeys = (char**)malloc(1024 * sizeof(char*));
    int* memoValues = (int*)malloc(1024 * sizeof(int));
    int memoSize = 0;
    char boardCopy[128];
    char handCopy[32];
    strcpy(boardCopy, board);
    strcpy(handCopy, hand);
    int result = dfs(boardCopy, handCopy, memoKeys, memoValues, &memoSize);
    for (int index = 0; index < memoSize; index++) {
        free(memoKeys[index]);
    }
    free(memoKeys);
    free(memoValues);
    return result == INT_MAX ? -1 : result;
}

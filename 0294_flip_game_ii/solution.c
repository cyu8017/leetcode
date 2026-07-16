// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct MemoEntry {
    char* state;
    bool canWin;
    struct MemoEntry* next;
} MemoEntry;

static bool memoContains(MemoEntry* head, const char* state, bool* canWin) {
    for (MemoEntry* current = head; current != NULL; current = current->next) {
        if (strcmp(current->state, state) == 0) {
            *canWin = current->canWin;
            return true;
        }
    }
    return false;
}

static void memoAdd(MemoEntry** head, const char* state, bool canWin) {
    MemoEntry* node = (MemoEntry*)malloc(sizeof(MemoEntry));
    node->state = strdup(state);
    node->canWin = canWin;
    node->next = *head;
    *head = node;
}

static void memoFree(MemoEntry* head) {
    while (head != NULL) {
        MemoEntry* next = head->next;
        free(head->state);
        free(head);
        head = next;
    }
}

static bool canWinState(const char* state, MemoEntry** memo) {
    bool cached;
    if (memoContains(*memo, state, &cached)) {
        return cached;
    }

    int length = (int)strlen(state);
    for (int index = 0; index + 1 < length; index++) {
        if (state[index] == '+' && state[index + 1] == '+') {
            char* nextState = strdup(state);
            nextState[index] = '-';
            nextState[index + 1] = '-';
            if (!canWinState(nextState, memo)) {
                free(nextState);
                memoAdd(memo, state, true);
                return true;
            }
            free(nextState);
        }
    }

    memoAdd(memo, state, false);
    return false;
}

bool canWin(char* currentState) {
    MemoEntry* memo = NULL;
    bool result = canWinState(currentState, &memo);
    memoFree(memo);
    return result;
}

// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char** items;
    int size;
    int capacity;
} StringQueue;

typedef struct {
    char** items;
    int size;
    int capacity;
} StringSet;

static bool isValid(const char* text) {
    int balance = 0;
    for (int index = 0; text[index] != '\0'; index++) {
        if (text[index] == '(') {
            balance += 1;
        } else if (text[index] == ')') {
            if (balance == 0) {
                return false;
            }
            balance -= 1;
        }
    }
    return balance == 0;
}

static void queuePush(StringQueue* queue, const char* value) {
    if (queue->size == queue->capacity) {
        queue->capacity = queue->capacity ? queue->capacity * 2 : 8;
        queue->items = realloc(queue->items, (size_t)queue->capacity * sizeof(char*));
    }
    queue->items[queue->size++] = strdup(value);
}

static char* queuePop(StringQueue* queue) {
    char* value = queue->items[0];
    for (int index = 1; index < queue->size; index++) {
        queue->items[index - 1] = queue->items[index];
    }
    queue->size -= 1;
    return value;
}

static bool setContains(StringSet* set, const char* value) {
    for (int index = 0; index < set->size; index++) {
        if (strcmp(set->items[index], value) == 0) {
            return true;
        }
    }
    return false;
}

static void setAdd(StringSet* set, const char* value) {
    if (setContains(set, value)) {
        return;
    }
    if (set->size == set->capacity) {
        set->capacity = set->capacity ? set->capacity * 2 : 8;
        set->items = realloc(set->items, (size_t)set->capacity * sizeof(char*));
    }
    set->items[set->size++] = strdup(value);
}

char** removeInvalidParentheses(char* s, int* returnSize) {
    *returnSize = 0;
    StringQueue queue = { NULL, 0, 0 };
    StringSet visited = { NULL, 0, 0 };
    StringSet result = { NULL, 0, 0 };
    queuePush(&queue, s);
    setAdd(&visited, s);
    bool found = false;

    while (queue.size > 0) {
        int levelSize = queue.size;
        for (int level = 0; level < levelSize; level++) {
            char* current = queuePop(&queue);
            if (isValid(current)) {
                setAdd(&result, current);
                found = true;
            }
            if (!found) {
                int length = (int)strlen(current);
                for (int index = 0; index < length; index++) {
                    if (current[index] != '(' && current[index] != ')') {
                        continue;
                    }
                    char* next = (char*)malloc((size_t)length);
                    strncpy(next, current, (size_t)index);
                    next[index] = '\0';
                    strcat(next, current + index + 1);
                    if (!setContains(&visited, next)) {
                        setAdd(&visited, next);
                        queuePush(&queue, next);
                    }
                    free(next);
                }
            }
            free(current);
        }
    }

    *returnSize = result.size;
    return result.items;
}

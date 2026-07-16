// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** items;
    int size;
    int capacity;
} StringList;

static void stringListInit(StringList* list) {
    list->items = NULL;
    list->size = 0;
    list->capacity = 0;
}

static void stringListPush(StringList* list, char* value) {
    if (list->size == list->capacity) {
        list->capacity = list->capacity == 0 ? 8 : list->capacity * 2;
        list->items = (char**)realloc(list->items, (size_t)list->capacity * sizeof(char*));
    }
    list->items[list->size++] = value;
}

static long long parseNumber(const char* num, int start, int end) {
    long long value = 0;
    for (int index = start; index <= end; index++) {
        value = value * 10 + (num[index] - '0');
    }
    return value;
}

static void appendString(char* dest, const char* src) {
    strcat(dest, src);
}

static void backtrack(
    const char* num,
    int numLength,
    int target,
    int index,
    char* path,
    long long value,
    long long previous,
    StringList* result
) {
    if (index == numLength) {
        if (value == target) {
            stringListPush(result, strdup(path));
        }
        return;
    }

    char segment[32];
    char nextPath[64];

    for (int end = index; end < numLength; end++) {
        if (end > index && num[index] == '0') {
            break;
        }
        int length = end - index + 1;
        memcpy(segment, num + index, (size_t)length);
        segment[length] = '\0';
        long long current = parseNumber(num, index, end);

        if (index == 0) {
            backtrack(num, numLength, target, end + 1, segment, current, current, result);
        } else {
            strcpy(nextPath, path);
            appendString(nextPath, "+");
            appendString(nextPath, segment);
            backtrack(num, numLength, target, end + 1, nextPath, value + current, current, result);

            strcpy(nextPath, path);
            appendString(nextPath, "-");
            appendString(nextPath, segment);
            backtrack(num, numLength, target, end + 1, nextPath, value - current, -current, result);

            strcpy(nextPath, path);
            appendString(nextPath, "*");
            appendString(nextPath, segment);
            backtrack(
                num,
                numLength,
                target,
                end + 1,
                nextPath,
                value - previous + previous * current,
                previous * current,
                result
            );
        }
    }
}

char** addOperators(char* num, int target, int* returnSize) {
    StringList result;
    stringListInit(&result);
    char path[64] = {0};
    backtrack(num, (int)strlen(num), target, 0, path, 0, 0, &result);
    *returnSize = result.size;
    return result.items;
}

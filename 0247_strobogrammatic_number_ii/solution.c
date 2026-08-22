// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char** items;
    int size;
    int capacity;
} StringList;

static void string_list_init(StringList* list) {
    list->items = NULL;
    list->size = 0;
    list->capacity = 0;
}

static void string_list_push(StringList* list, char* value) {
    if (list->size == list->capacity) {
        list->capacity = list->capacity == 0 ? 8 : list->capacity * 2;
        list->items = realloc(list->items, (size_t)list->capacity * sizeof(char*));
    }
    list->items[list->size++] = value;
}

static StringList build(int left, int right) {
    StringList result;
    string_list_init(&result);

    if (left > right) {
        string_list_push(&result, strdup(""));
        return result;
    }
    if (left == right) {
        string_list_push(&result, strdup("0"));
        string_list_push(&result, strdup("1"));
        string_list_push(&result, strdup("8"));
        return result;
    }

    static const char* starts[] = {"0", "1", "6", "8", "9"};
    static const char* ends[] = {"0", "1", "9", "8", "6"};
    for (int pair = 0; pair < 5; ++pair) {
        if (left == 0 && starts[pair][0] == '0') {
            continue;
        }
        StringList middles = build(left + 1, right - 1);
        for (int i = 0; i < middles.size; ++i) {
            size_t length = strlen(starts[pair]) + strlen(middles.items[i]) + strlen(ends[pair]) + 1;
            char* combined = malloc(length);
            snprintf(combined, length, "%s%s%s", starts[pair], middles.items[i], ends[pair]);
            string_list_push(&result, combined);
        }
        for (int i = 0; i < middles.size; ++i) {
            free(middles.items[i]);
        }
        free(middles.items);
    }
    return result;
}

char** findStrobogrammatic(int n, int* returnSize) {
    StringList built = build(0, n - 1);
    *returnSize = built.size;
    return built.items;
}

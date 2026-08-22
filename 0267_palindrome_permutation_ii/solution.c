// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** items;
    int size;
    int capacity;
} StringList;

static void string_list_add(StringList* list, const char* value) {
    if (list->size == list->capacity) {
        list->capacity = list->capacity ? list->capacity * 2 : 8;
        list->items = realloc(list->items, (size_t)list->capacity * sizeof(char*));
    }
    list->items[list->size++] = strdup(value);
}

static int compare_chars(const void* left, const void* right) {
    return (*(const char*)left) - (*(const char*)right);
}

static void backtrack(
    const char* half,
    int half_size,
    int* used,
    char* path,
    int depth,
    const char* middle,
    StringList* result) {
    if (depth == half_size) {
        char buffer[4096];
        snprintf(buffer, sizeof(buffer), "%s%s", path, middle);
        int length = (int)strlen(buffer);
        for (int i = depth - 1; i >= 0; i--) {
            buffer[length++] = path[i];
        }
        buffer[length] = '\0';
        string_list_add(result, buffer);
        return;
    }
    for (int index = 0; index < half_size; index++) {
        if (used[index]) {
            continue;
        }
        if (index > 0 && half[index] == half[index - 1] && !used[index - 1]) {
            continue;
        }
        used[index] = 1;
        path[depth] = half[index];
        backtrack(half, half_size, used, path, depth + 1, middle, result);
        used[index] = 0;
    }
}

char** generatePalindromes(char* s, int* returnSize) {
    *returnSize = 0;
    int counts[256] = {0};
    for (int index = 0; s[index] != '\0'; ++index) {
        counts[(unsigned char)s[index]]++;
    }

    char middle[2] = "";
    int odd_count = 0;
    for (int ch = 0; ch < 256; ++ch) {
        if (counts[ch] % 2 != 0) {
            middle[0] = (char)ch;
            odd_count++;
        }
    }
    if (odd_count > 1) {
        return NULL;
    }

    char keys[256];
    int key_count = 0;
    for (int ch = 0; ch < 256; ++ch) {
        if (counts[ch] > 0) {
            keys[key_count++] = (char)ch;
        }
    }
    qsort(keys, (size_t)key_count, sizeof(char), compare_chars);

    int half_size = 0;
    for (int i = 0; i < key_count; ++i) {
        half_size += counts[(unsigned char)keys[i]] / 2;
    }

    char* half = (char*)malloc((size_t)half_size + 1);
    int half_index = 0;
    for (int i = 0; i < key_count; ++i) {
        int repeat = counts[(unsigned char)keys[i]] / 2;
        for (int j = 0; j < repeat; ++j) {
            half[half_index++] = keys[i];
        }
    }
    half[half_size] = '\0';

    StringList result = { NULL, 0, 0 };
    int* used = (int*)calloc((size_t)half_size, sizeof(int));
    char* path = (char*)malloc((size_t)half_size + 1);
    backtrack(half, half_size, used, path, 0, middle, &result);

    free(half);
    free(used);
    free(path);
    *returnSize = result.size;
    return result.items;
}

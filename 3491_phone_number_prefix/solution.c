// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmp_str(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

bool phonePrefix(char** numbers, int numbersSize) {
    qsort(numbers, (size_t)numbersSize, sizeof(char*), cmp_str);
    for (int i = 0; i + 1 < numbersSize; i++) {
        int len = (int)strlen(numbers[i]);
        if ((int)strlen(numbers[i + 1]) >= len && strncmp(numbers[i + 1], numbers[i], (size_t)len) == 0)
            return false;
    }
    return true;
}

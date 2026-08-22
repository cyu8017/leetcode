// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void appendChar(char** buffer, int* length, int* capacity, char value) {
    if (*length + 1 >= *capacity) {
        *capacity *= 2;
        *buffer = (char*)realloc(*buffer, (size_t)(*capacity));
    }
    (*buffer)[(*length)++] = value;
    (*buffer)[*length] = '\0';
}

static void appendCount(char** buffer, int* length, int* capacity, int count) {
    char digits[12];
    int digitCount = sprintf(digits, "%d", count);
    for (int i = 0; i < digitCount; i++) {
        appendChar(buffer, length, capacity, digits[i]);
    }
}

char* countAndSay(int n) {
    int capacity = 64;
    char* term = (char*)malloc((size_t)capacity);
    strcpy(term, "1");

    for (int i = 1; i < n; i++) {
        int nextCapacity = (int)strlen(term) * 2 + 16;
        char* nextTerm = (char*)malloc((size_t)nextCapacity);
        int nextLength = 0;
        nextTerm[0] = '\0';

        int index = 0;
        int termLength = (int)strlen(term);
        while (index < termLength) {
            int count = 1;
            while (index + count < termLength && term[index + count] == term[index]) {
                count++;
            }
            appendCount(&nextTerm, &nextLength, &nextCapacity, count);
            appendChar(&nextTerm, &nextLength, &nextCapacity, term[index]);
            index += count;
        }

        free(term);
        term = nextTerm;
        capacity = nextCapacity;
    }

    return term;
}

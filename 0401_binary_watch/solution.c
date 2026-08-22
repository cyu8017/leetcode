// LeetCode 0401 - Binary Watch
// https://leetcode.com/problems/binary-watch/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int popcount(int value) {
    int count = 0;
    while (value) {
        count += value & 1;
        value >>= 1;
    }
    return count;
}

char** readBinaryWatch(int turnedOn, int* returnSize) {
    *returnSize = 0;
    char** result = NULL;
    int capacity = 0;

    for (int hour = 0; hour < 12; hour++) {
        for (int minute = 0; minute < 60; minute++) {
            if (popcount(hour) + popcount(minute) != turnedOn) {
                continue;
            }

            if (*returnSize == capacity) {
                capacity = capacity ? capacity * 2 : 16;
                result = (char**)realloc(result, (size_t)capacity * sizeof(char*));
            }

            char buffer[6];
            snprintf(buffer, sizeof(buffer), "%d:%02d", hour, minute);
            result[*returnSize] = (char*)malloc(strlen(buffer) + 1);
            strcpy(result[*returnSize], buffer);
            *returnSize += 1;
        }
    }

    return result;
}

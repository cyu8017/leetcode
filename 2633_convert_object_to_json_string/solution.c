// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// JavaScript problem; C stand-in stringifies an int array as JSON.
char* jsonStringifyInts(int* arr, int arrSize) {
    size_t cap = (size_t)arrSize * 12 + 3;
    char* out = (char*)malloc(cap);
    size_t len = 0;
    out[len++] = '[';
    for (int i = 0; i < arrSize; i++) {
        if (i) out[len++] = ',';
        len += (size_t)sprintf(out + len, "%d", arr[i]);
    }
    out[len++] = ']';
    out[len] = 0;
    return out;
}

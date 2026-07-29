// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* chars;
    int* counts;
    int size;
    int index;
} StringIterator;

StringIterator* stringIteratorCreate(char* compressedString) {
    StringIterator* obj = (StringIterator*)malloc(sizeof(StringIterator));
    int n = (int)strlen(compressedString);
    obj->chars = (char*)malloc((size_t)n + 1);
    obj->counts = (int*)malloc((size_t)n * sizeof(int));
    obj->size = 0;
    obj->index = 0;
    int i = 0;
    while (i < n) {
        char ch = compressedString[i++];
        int value = 0;
        while (i < n && isdigit((unsigned char)compressedString[i])) {
            value = value * 10 + (compressedString[i] - '0');
            i++;
        }
        obj->chars[obj->size] = ch;
        obj->counts[obj->size] = value;
        obj->size++;
    }
    return obj;
}

char stringIteratorNext(StringIterator* obj) {
    if (obj->index >= obj->size) {
        return ' ';
    }
    char ch = obj->chars[obj->index];
    obj->counts[obj->index]--;
    if (obj->counts[obj->index] == 0) {
        obj->index++;
    }
    return ch;
}

bool stringIteratorHasNext(StringIterator* obj) {
    return obj->index < obj->size;
}

void stringIteratorFree(StringIterator* obj) {
    free(obj->chars);
    free(obj->counts);
    free(obj);
}

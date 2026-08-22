// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

#include <stdlib.h>
#include <string.h>

char* createInfiniteObject(char* name) {
    if (!name) {
        char* e = (char*)malloc(1);
        e[0] = '\0';
        return e;
    }
    char* s = (char*)malloc(strlen(name) + 1);
    strcpy(s, name);
    return s;
}

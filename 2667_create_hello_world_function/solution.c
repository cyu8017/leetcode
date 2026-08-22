// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

#include <stdlib.h>
#include <string.h>

char* createHelloWorld(void) {
    char* s = (char*)malloc(12);
    strcpy(s, "Hello World");
    return s;
}

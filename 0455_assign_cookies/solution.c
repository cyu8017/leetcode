// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    qsort(g, (size_t)gSize, sizeof(int), cmpInt);
    qsort(s, (size_t)sSize, sizeof(int), cmpInt);
    int child = 0;
    int cookie = 0;
    while (child < gSize && cookie < sSize) {
        if (s[cookie] >= g[child]) {
            child++;
        }
        cookie++;
    }
    return child;
}

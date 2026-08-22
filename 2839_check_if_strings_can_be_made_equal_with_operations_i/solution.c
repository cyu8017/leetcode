// LeetCode 2839 - Check if Strings Can be Made Equal With Operations I
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

#include <stdbool.h>

static void sort2(char* a) {
    if (a[0] > a[1]) { char t = a[0]; a[0] = a[1]; a[1] = t; }
}

bool canBeEqual(char* s1, char* s2) {
    char a[2] = {s1[0], s1[2]}, b[2] = {s2[0], s2[2]};
    char c[2] = {s1[1], s1[3]}, d[2] = {s2[1], s2[3]};
    sort2(a); sort2(b); sort2(c); sort2(d);
    return a[0]==b[0] && a[1]==b[1] && c[0]==d[0] && c[1]==d[1];
}

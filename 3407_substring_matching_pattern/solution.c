// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

bool hasMatch(char* s, char* p) {
    char* star = strchr(p, '*');
    int li = (int)(star - p);
    char* left = (char*)malloc(li + 1);
    memcpy(left, p, li); left[li] = 0;
    char* right = star + 1;
    char* pos = strstr(s, left);
    free(left);
    if (!pos) return false;
    return strstr(pos + li, right) != NULL;
}

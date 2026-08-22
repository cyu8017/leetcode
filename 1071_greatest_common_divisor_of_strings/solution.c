// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

#include <stdlib.h>
#include <string.h>

static int gcdInt(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

char* gcdOfStrings(char* str1, char* str2) {
    int n1 = (int)strlen(str1);
    int n2 = (int)strlen(str2);
    char* a = (char*)malloc((size_t)n1 + (size_t)n2 + 1);
    char* b = (char*)malloc((size_t)n1 + (size_t)n2 + 1);
    strcpy(a, str1);
    strcat(a, str2);
    strcpy(b, str2);
    strcat(b, str1);
    if (strcmp(a, b) != 0) {
        free(a);
        free(b);
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    free(a);
    free(b);
    int g = gcdInt(n1, n2);
    char* ans = (char*)malloc((size_t)g + 1);
    memcpy(ans, str1, (size_t)g);
    ans[g] = '\0';
    return ans;
}

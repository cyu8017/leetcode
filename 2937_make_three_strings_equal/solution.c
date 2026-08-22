// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

#include <string.h>

int findMinimumOperations(char* s1, char* s2, char* s3) {
    int n = (int)strlen(s1), n2 = (int)strlen(s2), n3 = (int)strlen(s3);
    if (n2 < n) n = n2;
    if (n3 < n) n = n3;
    int i = 0;
    while (i < n && s1[i] == s2[i] && s2[i] == s3[i]) i++;
    if (i == 0) return -1;
    return (int)strlen(s1) + (int)strlen(s2) + (int)strlen(s3) - 3 * i;
}

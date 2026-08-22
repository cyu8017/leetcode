// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isTransformable(char* s, char* t) {
    int n = (int)strlen(s);
    int* positions[10];
    int front[10] = {0}, back[10] = {0};
    for (int d = 0; d < 10; d++) positions[d] = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int d = s[i] - '0';
        positions[d][back[d]++] = i;
    }
    for (int i = 0; i < n; i++) {
        int d = t[i] - '0';
        if (front[d] >= back[d]) {
            for (int x = 0; x < 10; x++) free(positions[x]);
            return false;
        }
        int index = positions[d][front[d]];
        for (int smaller = 0; smaller < d; smaller++) {
            if (front[smaller] < back[smaller] && positions[smaller][front[smaller]] < index) {
                for (int x = 0; x < 10; x++) free(positions[x]);
                return false;
            }
        }
        front[d]++;
    }
    for (int x = 0; x < 10; x++) free(positions[x]);
    return true;
}

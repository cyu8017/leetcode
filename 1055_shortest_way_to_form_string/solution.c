// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

#include <stdbool.h>
#include <string.h>

int shortestWay(char* source, char* target) {
    bool present[128] = {false};
    for (char* p = source; *p; p++) {
        present[(unsigned char)*p] = true;
    }
    for (char* p = target; *p; p++) {
        if (!present[(unsigned char)*p]) {
            return -1;
        }
    }
    int n = (int)strlen(target);
    int ans = 0;
    int i = 0;
    while (i < n) {
        ans++;
        for (char* p = source; *p && i < n; p++) {
            if (target[i] == *p) {
                i++;
            }
        }
    }
    return ans;
}

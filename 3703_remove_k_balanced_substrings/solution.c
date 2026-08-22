// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

#include <stdlib.h>
#include <string.h>

typedef struct { char ch; int count; } Pair;

char* removeSubstring(char* s, int k) {
    int n = (int)strlen(s);
    Pair* stk = (Pair*)malloc((size_t)(n + 1) * sizeof(Pair));
    int top = 0;
    for (int i = 0; i < n; i++) {
        char c = s[i];
        if (top > 0 && stk[top - 1].ch == c) stk[top - 1].count++;
        else { stk[top].ch = c; stk[top].count = 1; top++; }
        if (c == ')' && top > 1) {
            Pair* tp = &stk[top - 1];
            Pair* prev = &stk[top - 2];
            if (tp->count == k && prev->count >= k) {
                top--;
                prev->count -= k;
                if (prev->count == 0) top--;
            }
        }
    }
    int len = 0;
    for (int i = 0; i < top; i++) len += stk[i].count;
    char* res = (char*)malloc((size_t)(len + 1));
    int p = 0;
    for (int i = 0; i < top; i++) {
        for (int j = 0; j < stk[i].count; j++) res[p++] = stk[i].ch;
    }
    res[p] = 0;
    free(stk);
    return res;
}

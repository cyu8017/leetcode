// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int atoi_range(const char* s, int l, int r) {
    int v = 0;
    for (int i = l; i < r; i++) v = v * 10 + (s[i] - '0');
    return v;
}

char* minimizeResult(char* expression) {
    int plus = 0;
    int n = (int)strlen(expression);
    for (int i = 0; i < n; i++) if (expression[i] == '+') { plus = i; break; }
    int leftLen = plus, rightLen = n - plus - 1;
    int bestVal = INT_MAX;
    char* best = (char*)malloc((size_t)n + 3);
    best[0] = '\0';
    for (int i = 0; i < leftLen; i++) {
        for (int j = 1; j <= rightLen; j++) {
            // a = [0,i), b=[i,plus), c=[plus+1, plus+1+j), d=[plus+1+j, n)
            int bi = atoi_range(expression, i, plus);
            int ci = atoi_range(expression, plus + 1, plus + 1 + j);
            long long val = bi + ci;
            if (i > 0) val *= atoi_range(expression, 0, i);
            if (plus + 1 + j < n) val *= atoi_range(expression, plus + 1 + j, n);
            if ((int)val < bestVal) {
                bestVal = (int)val;
                int pos = 0;
                memcpy(best + pos, expression, (size_t)i); pos += i;
                best[pos++] = '(';
                memcpy(best + pos, expression + i, (size_t)(plus - i)); pos += plus - i;
                best[pos++] = '+';
                memcpy(best + pos, expression + plus + 1, (size_t)j); pos += j;
                best[pos++] = ')';
                memcpy(best + pos, expression + plus + 1 + j, (size_t)(n - plus - 1 - j));
                pos += n - plus - 1 - j;
                best[pos] = '\0';
            }
        }
    }
    return best;
}

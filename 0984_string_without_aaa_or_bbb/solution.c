// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

#include <stdlib.h>

char* strWithout3a3b(int a, int b) {
    char* ans = (char*)malloc((size_t)(a + b + 1));
    int n = 0;
    while (a || b) {
        int write_a;
        if (n >= 2 && ans[n - 1] == ans[n - 2]) write_a = (ans[n - 1] == 'b');
        else write_a = a >= b;
        if (write_a) { ans[n++] = 'a'; a--; }
        else { ans[n++] = 'b'; b--; }
    }
    ans[n] = 0;
    return ans;
}

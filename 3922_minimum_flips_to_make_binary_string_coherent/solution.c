// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

#include <string.h>

int minFlips(char* s) {
    int n = (int)strlen(s);
    int ones = 0;
    for (int i = 0; i < n; i++) if (s[i] == '1') ones++;
    int answer = ones;
    if (ones > 0) answer = ones - 1;
    int zeros = n - ones;
    if (zeros < answer) answer = zeros;
    if (n >= 2) {
        int cost = 0;
        for (int i = 0; i < n; i++) {
            char want = (i == 0 || i == n - 1) ? '1' : '0';
            if (s[i] != want) cost++;
        }
        if (cost < answer) answer = cost;
    }
    return answer;
}

// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

#include <string.h>

int maxNumberOfBalloons(char* text) {
    int count[256] = {0};
    for (int i = 0; text[i]; i++) count[(unsigned char)text[i]]++;
    int ans = count['b'];
    if (count['a'] < ans) ans = count['a'];
    if (count['l'] / 2 < ans) ans = count['l'] / 2;
    if (count['o'] / 2 < ans) ans = count['o'] / 2;
    if (count['n'] < ans) ans = count['n'];
    return ans;
}

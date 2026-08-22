// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

#include <string.h>

int maxDifference(char* s) {
    int freq[26] = {0};
    for (int i = 0; s[i]; i++) freq[s[i] - 'a']++;
    int maxOdd = 0, minEven = 1000000000;
    for (int i = 0; i < 26; i++) {
        int f = freq[i];
        if (!f) continue;
        if (f % 2 == 1) { if (f > maxOdd) maxOdd = f; }
        else if (f < minEven) minEven = f;
    }
    return maxOdd - minEven;
}

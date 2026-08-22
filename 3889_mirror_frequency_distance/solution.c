// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

#include <string.h>
#include <stdlib.h>

int mirrorFrequency(char* s) {
    int freq[128] = {0};
    for (int i = 0; s[i]; i++) freq[(unsigned char)s[i]]++;
    int ans = 0;
    int vis[128] = {0};
    for (int c = 0; c < 128; c++) {
        if (!freq[c]) continue;
        int m;
        if (c >= 'a' && c <= 'z') m = 'a' + 25 - (c - 'a');
        else if (c >= '0' && c <= '9') m = '0' + (9 - (c - '0'));
        else continue;
        if (vis[m]) continue;
        vis[c] = 1;
        int mv = freq[m];
        int d = freq[c] - mv;
        if (d < 0) d = -d;
        ans += d;
    }
    return ans;
}

// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

#include <string.h>
#include <stdlib.h>

int totalDistance(char* s) {
    static int pos[128][2];
    static int init = 0;
    if (!init) {
        init = 1;
        const char* keys[3] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; keys[i][j]; j++) {
                pos[(unsigned char)keys[i][j]][0] = i;
                pos[(unsigned char)keys[i][j]][1] = j;
            }
        }
    }
    unsigned char pre = 'a';
    int ans = 0;
    for (int i = 0; s[i]; i++) {
        unsigned char cur = (unsigned char)s[i];
        int dx = pos[pre][0] - pos[cur][0];
        int dy = pos[pre][1] - pos[cur][1];
        if (dx < 0) dx = -dx;
        if (dy < 0) dy = -dy;
        ans += dx + dy;
        pre = cur;
    }
    return ans;
}

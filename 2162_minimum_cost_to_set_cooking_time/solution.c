// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

#include <stdio.h>
#include <string.h>

static int cost2162(int startAt, int moveCost, int pushCost, int mins, int secs) {
    if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return 1 << 30;
    char s[8];
    if (mins > 0) sprintf(s, "%d%02d", mins, secs);
    else sprintf(s, "%d", secs);
    char cur = (char)('0' + startAt);
    int ans = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] != cur) { ans += moveCost; cur = s[i]; }
        ans += pushCost;
    }
    return ans;
}

int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
    int mins = targetSeconds / 60, secs = targetSeconds % 60;
    int ans = cost2162(startAt, moveCost, pushCost, mins, secs);
    if (mins > 0) {
        int c2 = cost2162(startAt, moveCost, pushCost, mins - 1, secs + 60);
        if (c2 < ans) ans = c2;
    }
    return ans;
}

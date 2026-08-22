// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

#include <string.h>

int countCollisions(char* directions) {
    int n = (int)strlen(directions);
    int i = 0, j = n - 1;
    while (i < n && directions[i] == 'L') i++;
    while (j >= 0 && directions[j] == 'R') j--;
    int ans = 0;
    for (int k = i; k <= j; k++) if (directions[k] != 'S') ans++;
    return ans;
}

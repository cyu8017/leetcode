// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

int numFriendRequests(int* ages, int agesSize) {
    int count[121] = {0};
    for (int i = 0; i < agesSize; i++) count[ages[i]]++;
    int ans = 0;
    for (int x = 1; x <= 120; x++) {
        if (!count[x]) continue;
        for (int y = 1; y <= 120; y++) {
            if (!count[y]) continue;
            if (y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100)) continue;
            ans += count[x] * count[y];
            if (x == y) ans -= count[x];
        }
    }
    return ans;
}

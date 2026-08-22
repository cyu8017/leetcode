// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

int maxDistance(char* s, int k) {
    int ans = 0, lat = 0, lon = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == 'N') lat++;
        else if (s[i] == 'S') lat--;
        else if (s[i] == 'E') lon++;
        else lon--;
        int md = lat < 0 ? -lat : lat;
        md += lon < 0 ? -lon : lon;
        int steps = i + 1;
        int cur = md + 2 * k;
        if (cur > steps) cur = steps;
        if (cur > ans) ans = cur;
    }
    return ans;
}

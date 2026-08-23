// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution {
    public int maxDistance(String s, int k) {
        int ans = 0;
        int lat = 0, lon = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'N') lat++;
            else if (c == 'S') lat--;
            else if (c == 'E') lon++;
            else lon--;
            int md = Math.abs(lat) + Math.abs(lon);
            int steps = i + 1;
            int cur = md + 2 * k;
            if (cur > steps) cur = steps;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}

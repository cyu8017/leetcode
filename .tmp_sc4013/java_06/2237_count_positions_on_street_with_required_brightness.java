// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

class Solution {
    public int meetRequirement(int n, int[][] lights, int[] requirement) {
        int[] diff = new int[n + 1];
        for (var light : lights) {
            int pos = light[0], r = light[1];
            int l = Math.max(0, pos - r);
            int rr = Math.min(n - 1, pos + r);
            diff[l]++;
            diff[rr + 1]--;
        }
        int ans = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            if (cur >= requirement[i]) ans++;
        }
        return ans;
    }
}

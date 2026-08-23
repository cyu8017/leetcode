// LeetCode 3964 - Minimum Lights To Illuminate A Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

using System;

public class Solution {
    public int MinLights(int[] lights) {
        int n = lights.Length;
        int[] d = new int[n];
        for (int i = 0; i < n; i++) {
            int v = lights[i];
            if (v > 0) {
                int l = Math.Max(0, i - v);
                int r = Math.Min(n - 1, i + v);
                d[l]++;
                if (r + 1 < n) d[r + 1]--;
            }
        }
        int s = 0, cnt = 0, ans = 0;
        foreach (int x in d) {
            s += x;
            if (s == 0) cnt++;
            else {
                ans += (cnt + 2) / 3;
                cnt = 0;
            }
        }
        ans += (cnt + 2) / 3;
        return ans;
    }
}

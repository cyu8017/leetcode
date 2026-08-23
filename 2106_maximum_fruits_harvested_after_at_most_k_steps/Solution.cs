// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

public class Solution {
    private int MinSteps(int left, int right, int start) {
        if (right <= start) return start - left;
        if (left >= start) return right - start;
        return Math.Min((start - left) + (right - left), (right - start) + (right - left));
    }

    public int MaxTotalFruits(int[][] fruits, int startPos, int k) {
        int n = fruits.Length;
        int[] pref = new int[n + 1], pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[i] = fruits[i][0];
            pref[i + 1] = pref[i] + fruits[i][1];
        }
        int ans = 0, j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && MinSteps(pos[i], pos[j], startPos) > k) j++;
            if (j <= i) ans = Math.Max(ans, pref[i + 1] - pref[j]);
        }
        j = 0;
        for (int i = 0; i < n; i++) {
            while (j <= i && MinSteps(pos[j], pos[i], startPos) > k) j++;
            ans = Math.Max(ans, pref[i + 1] - pref[j]);
        }
        return ans;
    }
}

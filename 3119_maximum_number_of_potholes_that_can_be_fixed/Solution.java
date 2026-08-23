// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

class Solution {
    public int maxPotholes(String road, int budget) {
        road = road + ".";
        int n = road.length();
        int[] cnt = new int[n];
        int k = 0, ans = 0;
        for (int i = 0; i < n; i++) {
            char c = road.charAt(i);
            if (c == 'x') k++;
            else if (k > 0) { cnt[k]++; k = 0; }
        }
        for (k = n - 1; k > 0 && budget > 0; k--) {
            int t = Math.min(budget / (k + 1), cnt[k]);
            ans += t * k;
            budget -= t * (k + 1);
            cnt[k - 1] += cnt[k] - t;
        }
        return ans;
    }
}

// LeetCode 1399 - Count Largest Group
// https://leetcode.com/problems/count-largest-group/

class Solution {
    public int countLargestGroup(int n) {
        int[] cnt = new int[37];
        int max = 0;
        for (int x = 1; x <= n; x++) {
            int s = 0, t = x;
            while (t > 0) {
                s += t % 10;
                t /= 10;
            }
            cnt[s]++;
            max = Math.max(max, cnt[s]);
        }
        int ans = 0;
        for (int v : cnt) if (v == max) ans++;
        return ans;
    }
}

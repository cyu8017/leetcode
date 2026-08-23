// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

public class Solution {
    public int NumberOfAlternatingGroups(int[] colors) {
        int k = 3, n = colors.Length, cnt = 0, ans = 0;
        for (int i = 0; i < n * 2; i++) {
            if (i > 0 && colors[i % n] == colors[(i - 1) % n]) cnt = 1;
            else cnt++;
            if (i >= n && cnt >= k) ans++;
        }
        return ans;
    }
}

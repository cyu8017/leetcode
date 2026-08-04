// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

class Solution {
    public int catchMaximumAmountofPeople(int[] team, int dist) {
        int ans = 0, j = 0, n = team.length;
        for (int i = 0; i < n; i++) {
            if (team[i] == 0) continue;
            while (j < n && (team[j] == 1 || i - j > dist)) j++;
            if (j < n && Math.abs(i - j) <= dist) {
                ans++;
                j++;
            }
        }
        return ans;
    }
}

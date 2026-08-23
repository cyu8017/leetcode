// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution {
    public int[] countOfPairs(int n, int x, int y) {
        int[] ans = new int[n];
        x--; y--;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = j - i;
                int b = Math.abs(x - i) + Math.abs(y - j) + 1;
                int c = Math.abs(x - j) + Math.abs(y - i) + 1;
                ans[Math.min(a, Math.min(b, c)) - 1] += 2;
            }
        }
        return ans;
    }
}

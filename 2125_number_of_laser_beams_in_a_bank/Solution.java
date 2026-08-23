// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution {
    public int numberOfBeams(String[] bank) {
        int ans = 0, prev = 0;
        for (String row : bank) {
            int cnt = 0;
            for (int i = 0; i < row.length(); i++) if (row.charAt(i) == '1') cnt++;
            if (cnt > 0) {
                ans += prev * cnt;
                prev = cnt;
            }
        }
        return ans;
    }
}

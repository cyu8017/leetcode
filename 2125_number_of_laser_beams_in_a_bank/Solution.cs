// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

public class Solution {
    public int NumberOfBeams(string[] bank) {
        int ans = 0, prev = 0;
        foreach (string row in bank) {
            int cnt = 0;
            foreach (char c in row) if (c == '1') cnt++;
            if (cnt > 0) {
                ans += prev * cnt;
                prev = cnt;
            }
        }
        return ans;
    }
}

// LeetCode 2678 - Number of Senior Citizens
// https://leetcode.com/problems/number-of-senior-citizens/

public class Solution {
    public int CountSeniors(string[] details) {
        int ans = 0;
        foreach (var d in details) {
            int age = (d[11] - '0') * 10 + (d[12] - '0');
            if (age > 60) ans++;
        }
        return ans;
    }
}

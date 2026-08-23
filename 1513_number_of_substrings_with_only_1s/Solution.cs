// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

public class Solution {
    public int NumSub(string s) {
        long ans = 0;
        int run = 0;
        foreach (char ch in s) {
            run = ch == '1' ? run + 1 : 0;
            ans += run;
        }
        return (int)(ans % 1000000007);
    }
}

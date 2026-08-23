// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

public class Solution {
    public int CountMonobit(int n) {
        int ans = 1;
        for (int i = 1, x = 1; x <= n; i++) {
            ans++;
            x += (1 << i);
        }
        return ans;
    }
}

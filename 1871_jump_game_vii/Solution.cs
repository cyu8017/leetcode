// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

public class Solution {
    public bool CanReach(string s, int minJump, int maxJump) {
        int n = s.Length;
        var reachable = new bool[n];
        reachable[0] = true;
        var prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (i > 0 && s[i] == '0') {
                int left = Math.Max(0, i - maxJump);
                int right = i - minJump;
                if (right >= left && prefix[right + 1] - prefix[left] > 0) {
                    reachable[i] = true;
                }
            }
            prefix[i + 1] = prefix[i] + (reachable[i] ? 1 : 0);
        }
        return reachable[n - 1];
    }
}

// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int n = s.length();
        boolean[] reachable = new boolean[n];
        reachable[0] = true;
        int[] prefix = new int[n + 1];

        for (int i = 0; i < n; i++) {
            if (i > 0 && s.charAt(i) == '0') {
                int left = Math.max(0, i - maxJump);
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

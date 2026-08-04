// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

class Solution {
    public int calculateTime(String keyboard, String word) {
        int[] pos = new int[26];
        for (int i = 0; i < keyboard.length(); i++) pos[keyboard.charAt(i) - 'a'] = i;
        int ans = 0, prev = 0;
        for (char ch : word.toCharArray()) {
            ans += Math.abs(pos[ch - 'a'] - prev);
            prev = pos[ch - 'a'];
        }
        return ans;
    }
}

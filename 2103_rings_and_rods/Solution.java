// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

class Solution {
    public int countPoints(String rings) {
        int[] mask = new int[10];
        for (int i = 0; i < rings.length(); i += 2) {
            char c = rings.charAt(i);
            int r = rings.charAt(i + 1) - '0';
            int bit = c == 'R' ? 1 : c == 'G' ? 2 : 4;
            mask[r] |= bit;
        }
        int ans = 0;
        for (int m : mask) if (m == 7) ans++;
        return ans;
    }
}

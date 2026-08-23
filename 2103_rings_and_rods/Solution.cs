// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

public class Solution {
    public int CountPoints(string rings) {
        int[] mask = new int[10];
        for (int i = 0; i < rings.Length; i += 2) {
            char c = rings[i];
            int r = rings[i + 1] - '0';
            int bit = c == 'R' ? 1 : c == 'G' ? 2 : 4;
            mask[r] |= bit;
        }
        int ans = 0;
        foreach (int m in mask) if (m == 7) ans++;
        return ans;
    }
}

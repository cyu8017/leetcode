// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

public class Solution {
    public int MinimumSwap(string s1, string s2) {
        int xy = 0, yx = 0;
        for (int i = 0; i < s1.Length; i++) {
            if (s1[i] == 'x' && s2[i] == 'y') xy++;
            if (s1[i] == 'y' && s2[i] == 'x') yx++;
        }
        if ((xy + yx) % 2 != 0) return -1;
        return xy / 2 + yx / 2 + 2 * (xy % 2);
    }
}

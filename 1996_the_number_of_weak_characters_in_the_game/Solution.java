// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

import java.util.*;

class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(b[1], a[1]));
        int ans = 0, maxDef = 0;
        for (int i = properties.length - 1; i >= 0; i--) {
            if (properties[i][1] < maxDef) ans++;
            else maxDef = properties[i][1];
        }
        return ans;
    }
}

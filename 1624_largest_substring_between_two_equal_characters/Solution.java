// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

import java.util.*;

class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int[] first = new int[26];
        Arrays.fill(first, -1);
        int ans = -1;
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] >= 0) ans = Math.max(ans, i - first[c] - 1);
            else first[c] = i;
        }
        return ans;
    }
}

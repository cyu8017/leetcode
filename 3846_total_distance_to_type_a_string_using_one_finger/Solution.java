// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private static final Map<Character, int[]> POS = buildPos();

    private static Map<Character, int[]> buildPos() {
        Map<Character, int[]> pos = new HashMap<>();
        String[] keys = { "qwertyuiop", "asdfghjkl", "zxcvbnm" };
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < keys[i].length(); j++) {
                pos.put(keys[i].charAt(j), new int[] { i, j });
            }
        }
        return pos;
    }

    public int totalDistance(String s) {
        char pre = 'a';
        int ans = 0;
        for (char cur : s.toCharArray()) {
            int[] p1 = POS.get(pre);
            int[] p2 = POS.get(cur);
            ans += Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
            pre = cur;
        }
        return ans;
    }
}

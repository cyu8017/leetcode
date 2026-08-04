// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

import java.util.*;

class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        Set<Long> occupied = new HashSet<>();
        for (int[] q : queens) occupied.add(key(q[0], q[1]));
        List<List<Integer>> answer = new ArrayList<>();
        for (int dr = -1; dr <= 1; dr++) {
            for (int dc = -1; dc <= 1; dc++) {
                if (dr == 0 && dc == 0) continue;
                int r = king[0] + dr, c = king[1] + dc;
                while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                    if (occupied.contains(key(r, c))) {
                        answer.add(Arrays.asList(r, c));
                        break;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }
        return answer;
    }

    private long key(int r, int c) {
        return ((long) r << 32) | (c & 0xffffffffL);
    }
}


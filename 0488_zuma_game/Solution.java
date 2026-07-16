// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private final Map<String, Integer> memo = new HashMap<>();

    public int findMinStep(String board, String hand) {
        int result = dfs(board, hand);
        return result == Integer.MAX_VALUE ? -1 : result;
    }

    private int dfs(String board, String hand) {
        String key = board + "|" + hand;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        board = shrink(board);
        if (board.isEmpty()) {
            memo.put(key, 0);
            return 0;
        }
        int best = Integer.MAX_VALUE;
        for (int i = 0; i <= board.length(); i++) {
            for (int j = 0; j < hand.length(); j++) {
                char color = hand.charAt(j);
                if (i < board.length() && board.charAt(i) == color) {
                    // valid insertion
                } else if (i > 0 && board.charAt(i - 1) == color) {
                    // valid insertion
                } else {
                    continue;
                }
                String newBoard = shrink(board.substring(0, i) + color + board.substring(i));
                if (newBoard.equals(board)) {
                    continue;
                }
                String newHand = hand.substring(0, j) + hand.substring(j + 1);
                int steps = dfs(newBoard, newHand);
                if (steps != Integer.MAX_VALUE) {
                    best = Math.min(best, steps + 1);
                }
            }
        }
        memo.put(key, best);
        return best;
    }

    private String shrink(String s) {
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (j < s.length() && s.charAt(j) == s.charAt(i)) {
                j += 1;
            }
            if (j - i >= 3) {
                return shrink(s.substring(0, i) + s.substring(j));
            }
            i = j;
        }
        return s;
    }
}

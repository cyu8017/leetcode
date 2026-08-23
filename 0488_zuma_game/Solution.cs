// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

public class Solution {
    private readonly Dictionary<string, int> memo = new();

    public int FindMinStep(string board, string hand) {
        int result = Dfs(board, hand);
        return result == int.MaxValue ? -1 : result;
    }

    private int Dfs(string board, string hand) {
        string key = board + "|" + hand;
        if (memo.TryGetValue(key, out int cached)) {
            return cached;
        }
        board = Shrink(board);
        if (board.Length == 0) {
            memo[key] = 0;
            return 0;
        }
        int best = int.MaxValue;
        for (int i = 0; i <= board.Length; i++) {
            for (int j = 0; j < hand.Length; j++) {
                char color = hand[j];
                bool valid = (i < board.Length && board[i] == color)
                    || (i > 0 && board[i - 1] == color);
                if (!valid) {
                    continue;
                }
                string newBoard = Shrink(board[..i] + color + board[i..]);
                if (newBoard == board) {
                    continue;
                }
                string newHand = hand.Remove(j, 1);
                int steps = Dfs(newBoard, newHand);
                if (steps != int.MaxValue) {
                    best = Math.Min(best, steps + 1);
                }
            }
        }
        memo[key] = best;
        return best;
    }

    private static string Shrink(string s) {
        int i = 0;
        while (i < s.Length) {
            int j = i;
            while (j < s.Length && s[j] == s[i]) {
                j += 1;
            }
            if (j - i >= 3) {
                return Shrink(s[..i] + s[j..]);
            }
            i = j;
        }
        return s;
    }
}

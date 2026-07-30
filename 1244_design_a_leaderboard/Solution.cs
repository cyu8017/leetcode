// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

using System.Collections.Generic;
using System.Linq;

public class Leaderboard {
    private readonly Dictionary<int, int> scores = new Dictionary<int, int>();

    public Leaderboard() {
    }

    public void AddScore(int playerId, int score) {
        scores[playerId] = scores.GetValueOrDefault(playerId) + score;
    }

    public int Top(int k) {
        return scores.Values.OrderByDescending(x => x).Take(k).Sum();
    }

    public void Reset(int playerId) {
        scores.Remove(playerId);
    }
}

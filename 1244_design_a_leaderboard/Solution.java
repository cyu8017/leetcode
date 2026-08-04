// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

import java.util.*;

class Leaderboard {
    private final Map<Integer, Integer> scores = new HashMap<>();

    public Leaderboard() {}

    public void addScore(int playerId, int score) {
        scores.put(playerId, scores.getOrDefault(playerId, 0) + score);
    }

    public int top(int K) {
        List<Integer> values = new ArrayList<>(scores.values());
        values.sort(Collections.reverseOrder());
        int sum = 0;
        for (int i = 0; i < Math.min(K, values.size()); i++) sum += values.get(i);
        return sum;
    }

    public void reset(int playerId) {
        scores.remove(playerId);
    }
}


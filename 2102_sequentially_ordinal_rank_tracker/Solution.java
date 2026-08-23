// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

import java.util.*;

class SORTracker {
    private static class Loc {
        String name;
        int score;
        Loc(String name, int score) { this.name = name; this.score = score; }
    }

    private final PriorityQueue<Loc> best = new PriorityQueue<>((a, b) -> {
        if (a.score != b.score) return Integer.compare(a.score, b.score);
        return b.name.compareTo(a.name);
    });
    private final PriorityQueue<Loc> rest = new PriorityQueue<>((a, b) -> {
        if (a.score != b.score) return Integer.compare(b.score, a.score);
        return a.name.compareTo(b.name);
    });
    private int k = 0;

    public SORTracker() {}

    public void add(String name, int score) {
        best.offer(new Loc(name, score));
        if (best.size() > k) rest.offer(best.poll());
    }

    public String get() {
        k++;
        if (!rest.isEmpty()) best.offer(rest.poll());
        return best.peek().name;
    }
}

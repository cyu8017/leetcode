// CONFIG class=Solution method=minGenerations types=None
// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

class Solution {
    static class P {
        final int a, b, c;
        P(int a, int b, int c) { this.a = a; this.b = b; this.c = c; }
        @Override public boolean equals(Object o) {
            if (!(o instanceof P)) return false;
            P p = (P) o;
            return a == p.a && b == p.b && c == p.c;
        }
        @Override public int hashCode() { return Objects.hash(a, b, c); }
    }

    public int minGenerations(int[][] points, int[] target) {
        P targetPoint = new P(target[0], target[1], target[2]);
        Map<P, Integer> generation = new HashMap<>();
        List<P> all = new ArrayList<>();
        for (int[] values : points) {
            P p = new P(values[0], values[1], values[2]);
            generation.put(p, 0);
            all.add(p);
        }
        if (generation.containsKey(targetPoint)) return generation.get(targetPoint);
        for (int current = 1; ; current++) {
            int limit = all.size();
            List<P> added = new ArrayList<>();
            for (int i = 0; i < limit; i++) {
                for (int j = i + 1; j < limit; j++) {
                    if (all.get(i).equals(all.get(j))) continue;
                    P pi = all.get(i), pj = all.get(j);
                    P p = new P((pi.a + pj.a) / 2, (pi.b + pj.b) / 2, (pi.c + pj.c) / 2);
                    if (!generation.containsKey(p)) {
                        generation.put(p, current);
                        added.add(p);
                    }
                }
            }
            if (generation.containsKey(targetPoint)) return generation.get(targetPoint);
            if (added.isEmpty()) return -1;
            all.addAll(added);
        }
    }
}

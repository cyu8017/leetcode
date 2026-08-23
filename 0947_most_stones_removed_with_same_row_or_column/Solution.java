// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

import java.util.*;

class Solution {
    private Map<Integer, Integer> parent = new HashMap<>();

    public int removeStones(int[][] stones) {
        for (int[] s : stones) unite(s[0], ~s[1]);
        Set<Integer> roots = new HashSet<>();
        for (int[] s : stones) roots.add(find(s[0]));
        return stones.length - roots.size();
    }

    private int find(int x) {
        if (!parent.containsKey(x)) parent.put(x, x);
        if (parent.get(x) != x) parent.put(x, find(parent.get(x)));
        return parent.get(x);
    }

    private void unite(int a, int b) {
        parent.put(find(a), find(b));
    }
}

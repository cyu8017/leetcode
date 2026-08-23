// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

import java.util.*;

class Solution {
    private Map<Integer, Integer> parent = new HashMap<>();
    private Map<Integer, Integer> size = new HashMap<>();

    private int find(int x) {
        if (parent.get(x) != x) parent.put(x, find(parent.get(x)));
        return parent.get(x);
    }

    private void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        if (size.get(ra) < size.get(rb)) { int t = ra; ra = rb; rb = t; }
        parent.put(rb, ra);
        size.put(ra, size.get(ra) + size.get(rb));
    }

    private int maskOf(String w) {
        int m = 0;
        for (int i = 0; i < w.length(); i++) m |= 1 << (w.charAt(i) - 'a');
        return m;
    }

    public int[] groupStrings(String[] words) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (String w : words) freq.merge(maskOf(w), 1, Integer::sum);
        for (Map.Entry<Integer, Integer> kv : freq.entrySet()) {
            parent.put(kv.getKey(), kv.getKey());
            size.put(kv.getKey(), kv.getValue());
        }
        for (int m : new ArrayList<>(freq.keySet())) {
            for (int b = 0; b < 26; b++) {
                if ((m & (1 << b)) != 0) {
                    int nm = m ^ (1 << b);
                    if (freq.containsKey(nm)) unite(m, nm);
                    for (int a = 0; a < 26; a++) {
                        if ((nm & (1 << a)) == 0) {
                            int rm = nm | (1 << a);
                            if (freq.containsKey(rm)) unite(m, rm);
                        }
                    }
                } else {
                    int nm = m | (1 << b);
                    if (freq.containsKey(nm)) unite(m, nm);
                }
            }
        }
        int groups = 0, maxSize = 0;
        Set<Integer> seen = new HashSet<>();
        for (int m : freq.keySet()) {
            int r = find(m);
            if (seen.add(r)) {
                groups++;
                maxSize = Math.max(maxSize, size.get(r));
            }
        }
        return new int[] {groups, maxSize};
    }
}

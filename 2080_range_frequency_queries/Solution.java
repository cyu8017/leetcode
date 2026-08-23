// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

import java.util.*;

class RangeFreqQuery {
    private final Map<Integer, List<Integer>> pos = new HashMap<>();

    public RangeFreqQuery(int[] arr) {
        for (int i = 0; i < arr.length; i++)
            pos.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
    }

    public int query(int left, int right, int value) {
        List<Integer> p = pos.get(value);
        if (p == null) return 0;
        return upper(p, right) - lower(p, left);
    }

    private int lower(List<Integer> p, int x) {
        int lo = 0, hi = p.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (p.get(mid) < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int upper(List<Integer> p, int x) {
        int lo = 0, hi = p.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (p.get(mid) <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

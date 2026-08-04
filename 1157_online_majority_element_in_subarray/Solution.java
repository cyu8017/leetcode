// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

import java.util.*;

class MajorityChecker {
    private final int[] arr;
    private final Map<Integer, List<Integer>> pos = new HashMap<>();

    public MajorityChecker(int[] arr) {
        this.arr = arr;
        for (int i = 0; i < arr.length; i++) {
            pos.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int query(int left, int right, int threshold) {
        int candidate = 0, count = 0;
        for (int i = left; i <= right; i++) {
            if (count == 0) candidate = arr[i];
            count += arr[i] == candidate ? 1 : -1;
        }
        List<Integer> locs = pos.get(candidate);
        int freq = upperBound(locs, right) - lowerBound(locs, left);
        return freq >= threshold ? candidate : -1;
    }

    private int lowerBound(List<Integer> a, int t) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < t) lo = mid + 1; else hi = mid;
        }
        return lo;
    }

    private int upperBound(List<Integer> a, int t) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) <= t) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}

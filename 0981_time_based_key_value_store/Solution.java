// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

import java.util.*;

class TimeMap {
    private final Map<String, List<Integer>> times = new HashMap<>();
    private final Map<String, List<String>> vals = new HashMap<>();

    public TimeMap() {}

    public void set(String key, String value, int timestamp) {
        times.computeIfAbsent(key, k -> new ArrayList<>()).add(timestamp);
        vals.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
    }

    public String get(String key, int timestamp) {
        List<Integer> tarr = times.get(key);
        if (tarr == null) return "";
        List<String> varr = vals.get(key);
        int lo = 0, hi = tarr.size() - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (tarr.get(mid) <= timestamp) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans < 0 ? "" : varr.get(ans);
    }
}

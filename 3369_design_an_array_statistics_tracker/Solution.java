// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class StatisticsTracker {
    private final List<Integer> arr = new ArrayList<>();
    private long sum = 0;
    private final Map<Integer, Integer> freq = new HashMap<>();
    private int modeFreq = 0;
    private final Set<Integer> modes = new HashSet<>();

    public StatisticsTracker() {}

    public void addNumber(int num) {
        arr.add(num);
        sum += num;
        int f = freq.merge(num, 1, Integer::sum);
        if (f > modeFreq) {
            modeFreq = f;
            modes.clear();
            modes.add(num);
        } else if (f == modeFreq) {
            modes.add(num);
        }
    }

    public void removeFirst() {
        if (arr.isEmpty()) return;
        int num = arr.remove(0);
        sum -= num;
        int f = freq.get(num) - 1;
        if (f == 0) freq.remove(num);
        else freq.put(num, f);
        modeFreq = 0;
        modes.clear();
        for (Map.Entry<Integer, Integer> e : freq.entrySet()) {
            int v = e.getKey(), ff = e.getValue();
            if (ff > modeFreq) {
                modeFreq = ff;
                modes.clear();
                modes.add(v);
            } else if (ff == modeFreq) {
                modes.add(v);
            }
        }
    }

    public int getMean() {
        if (arr.isEmpty()) return 0;
        return (int) (sum / arr.size());
    }

    public int getMedian() {
        int n = arr.size();
        List<Integer> tmp = new ArrayList<>(arr);
        Collections.sort(tmp);
        if (n % 2 == 1) return tmp.get(n / 2);
        return tmp.get(n / 2 - 1);
    }

    public int getMode() {
        long best = Long.MAX_VALUE;
        for (int v : modes) if (v < best) best = v;
        if (best == Long.MAX_VALUE) return 0;
        return (int) best;
    }
}

// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

import java.util.*;

class SnapshotArray {
    private int snapId;
    private final List<int[]>[] data;

    public SnapshotArray(int length) {
        snapId = 0;
        data = new List[length];
        for (int i = 0; i < length; i++) {
            data[i] = new ArrayList<>();
            data[i].add(new int[]{0, 0});
        }
    }

    public void set(int index, int val) {
        List<int[]> hist = data[index];
        int[] last = hist.get(hist.size() - 1);
        if (last[0] == snapId) last[1] = val;
        else hist.add(new int[]{snapId, val});
    }

    public int snap() {
        return snapId++;
    }

    public int get(int index, int snap_id) {
        List<int[]> hist = data[index];
        int lo = 0, hi = hist.size() - 1, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (hist.get(mid)[0] <= snap_id) {
                ans = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        return hist.get(ans)[1];
    }
}

// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

using System.Collections.Generic;

public class SnapshotArray {
    private int snapId;
    private readonly List<(int snap, int val)>[] data;

    public SnapshotArray(int length) {
        snapId = 0;
        data = new List<(int, int)>[length];
        for (int i = 0; i < length; i++) {
            data[i] = new List<(int, int)> { (0, 0) };
        }
    }

    public void Set(int index, int val) {
        var hist = data[index];
        if (hist[hist.Count - 1].snap == snapId) {
            hist[hist.Count - 1] = (snapId, val);
        } else {
            hist.Add((snapId, val));
        }
    }

    public int Snap() {
        return snapId++;
    }

    public int Get(int index, int snap_id) {
        var hist = data[index];
        int lo = 0, hi = hist.Count - 1, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (hist[mid].snap <= snap_id) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hist[ans].val;
    }
}

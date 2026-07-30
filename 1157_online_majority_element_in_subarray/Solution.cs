// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

using System.Collections.Generic;

public class MajorityChecker {
    private readonly int[] arr;
    private readonly Dictionary<int, List<int>> pos = new Dictionary<int, List<int>>();

    public MajorityChecker(int[] arr) {
        this.arr = arr;
        for (int i = 0; i < arr.Length; i++) {
            if (!pos.ContainsKey(arr[i])) pos[arr[i]] = new List<int>();
            pos[arr[i]].Add(i);
        }
    }

    public int Query(int left, int right, int threshold) {
        int candidate = 0, count = 0;
        for (int i = left; i <= right; i++) {
            if (count == 0) candidate = arr[i];
            count += arr[i] == candidate ? 1 : -1;
        }
        var locs = pos[candidate];
        int lo = LowerBound(locs, left);
        int hi = LowerBound(locs, right + 1);
        return hi - lo >= threshold ? candidate : -1;
    }

    private int LowerBound(List<int> locs, int target) {
        int lo = 0, hi = locs.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (locs[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

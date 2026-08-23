// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

using System.Collections.Generic;

public class RangeFreqQuery {
    private readonly Dictionary<int, List<int>> pos = new();

    public RangeFreqQuery(int[] arr) {
        for (int i = 0; i < arr.Length; i++) {
            if (!pos.ContainsKey(arr[i])) pos[arr[i]] = new List<int>();
            pos[arr[i]].Add(i);
        }
    }

    public int Query(int left, int right, int value) {
        if (!pos.TryGetValue(value, out var p)) return 0;
        int Lower(int x) {
            int lo = 0, hi = p.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (p[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
        int Upper(int x) {
            int lo = 0, hi = p.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (p[mid] <= x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
        return Upper(right) - Lower(left);
    }
}

// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MaxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        Array.Sort(tasks);
        Array.Sort(workers);
        bool Can(int k) {
            if (k == 0) return true;
            var ws = new SortedDictionary<int, int>();
            void Add(int x) { if (!ws.ContainsKey(x)) ws[x] = 0; ws[x]++; }
            void Remove(int x) { if (--ws[x] == 0) ws.Remove(x); }
            for (int i = workers.Length - k; i < workers.Length; i++) Add(workers[i]);
            int p = pills;
            for (int i = k - 1; i >= 0; i--) {
                int task = tasks[i];
                int strongest = ws.Keys.Last();
                if (strongest >= task) { Remove(strongest); continue; }
                if (p == 0) return false;
                int need = task - strength;
                int? found = null;
                foreach (var key in ws.Keys) {
                    if (key >= need) { found = key; break; }
                }
                if (found == null) return false;
                Remove(found.Value);
                p--;
            }
            return true;
        }
        int lo = 0, hi = Math.Min(tasks.Length, workers.Length);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}

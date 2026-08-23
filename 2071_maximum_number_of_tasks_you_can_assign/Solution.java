// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

import java.util.*;

class Solution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        Arrays.sort(tasks);
        Arrays.sort(workers);
        int lo = 0, hi = Math.min(tasks.length, workers.length);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(tasks, workers, pills, strength, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean can(int[] tasks, int[] workers, int pills, int strength, int k) {
        if (k == 0) return true;
        TreeMap<Integer, Integer> ws = new TreeMap<>();
        for (int i = workers.length - k; i < workers.length; i++)
            ws.merge(workers[i], 1, Integer::sum);
        int p = pills;
        for (int i = k - 1; i >= 0; i--) {
            int task = tasks[i];
            Integer strongest = ws.lastKey();
            if (strongest >= task) {
                remove(ws, strongest);
                continue;
            }
            if (p == 0) return false;
            int need = task - strength;
            Integer found = ws.ceilingKey(need);
            if (found == null) return false;
            remove(ws, found);
            p--;
        }
        return true;
    }

    private void remove(TreeMap<Integer, Integer> ws, int x) {
        int c = ws.get(x);
        if (c == 1) ws.remove(x);
        else ws.put(x, c - 1);
    }
}

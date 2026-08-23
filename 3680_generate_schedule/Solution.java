// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<int[]> matches;
    private boolean[] used;
    private List<int[]> sched;
    private int last0, last1;

    private boolean dfs() {
        if (sched.size() == matches.size()) return true;
        for (int i = 0; i < matches.size(); i++) {
            if (used[i]) continue;
            int[] m = matches.get(i);
            if (m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1) continue;
            used[i] = true;
            sched.add(m);
            int p0 = last0, p1 = last1;
            last0 = m[0];
            last1 = m[1];
            if (dfs()) return true;
            last0 = p0;
            last1 = p1;
            sched.remove(sched.size() - 1);
            used[i] = false;
        }
        return false;
    }

    public int[][] generateSchedule(int n) {
        if (n < 5) return new int[0][];
        matches = new ArrayList<>();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (i != j) matches.add(new int[] {i, j});
        used = new boolean[matches.size()];
        sched = new ArrayList<>();
        last0 = last1 = -1;
        if (dfs()) return sched.toArray(new int[0][]);
        return new int[0][];
    }
}

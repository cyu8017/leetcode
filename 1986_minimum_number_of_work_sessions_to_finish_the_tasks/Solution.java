// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution {
    public int minSessions(int[] tasks, int sessionTime) {
        int n = tasks.length;
        int[] sessions = new int[1 << n];
        int[] used = new int[1 << n];
        for (int i = 0; i < (1 << n); i++) {
            sessions[i] = n + 1;
            used[i] = 0;
        }
        sessions[0] = 1;
        used[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (sessions[mask] > n) continue;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                int nmask = mask | (1 << i);
                int ns, nu;
                if (used[mask] + tasks[i] <= sessionTime) {
                    ns = sessions[mask];
                    nu = used[mask] + tasks[i];
                } else {
                    ns = sessions[mask] + 1;
                    nu = tasks[i];
                }
                if (ns < sessions[nmask] || (ns == sessions[nmask] && nu < used[nmask])) {
                    sessions[nmask] = ns;
                    used[nmask] = nu;
                }
            }
        }
        return sessions[(1 << n) - 1];
    }
}

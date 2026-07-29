// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

#include <stdlib.h>

int minSessions(int* tasks, int tasksSize, int sessionTime) {
    int n = tasksSize;
    int N = 1 << n;
    int* sessions = (int*)malloc((size_t)N * sizeof(int));
    int* used = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) { sessions[i] = n + 1; used[i] = 0; }
    sessions[0] = 1; used[0] = 0;
    for (int mask = 0; mask < N; mask++) {
        if (sessions[mask] > n) continue;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) continue;
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
    int ans = sessions[N - 1];
    free(sessions); free(used);
    return ans;
}

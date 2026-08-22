// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

int hardestWorker(int n, int** logs, int logsSize, int* logsColSize) {
    (void)n; (void)logsColSize;
    int ans = logs[0][0], best = logs[0][1], prev = 0;
    for (int i = 0; i < logsSize; i++) {
        int dur = logs[i][1] - prev;
        if (dur > best || (dur == best && logs[i][0] < ans)) {
            best = dur; ans = logs[i][0];
        }
        prev = logs[i][1];
    }
    return ans;
}

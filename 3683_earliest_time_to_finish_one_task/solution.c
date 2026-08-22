// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

int earliestTime(int** tasks, int tasksSize, int* tasksColSize) {
    (void)tasksColSize;
    int ans = 2000000000;
    for (int i = 0; i < tasksSize; i++) {
        int v = tasks[i][0] + tasks[i][1];
        if (v < ans) ans = v;
    }
    return ans;
}

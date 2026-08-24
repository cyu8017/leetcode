// CONFIG class=Solution method=countTasks types=None
// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

class Solution {
    public int[] countTasks(int[] tasks, int[] shifts) {
        int m = tasks.length, n = shifts.length;
        long[] s = new long[m + 1];
        for (int i = 0; i < m; i++) s[i + 1] = s[i] + tasks[i];
        int[] ans = new int[n];
        int iIdx = 0;
        long cur = 0;
        for (int j = 0; j < n; j++) {
            if ((long)shifts[j] < (long)tasks[iIdx] - cur) {
                cur += shifts[j];
                ans[j] = m - iIdx;
            } else {
                long t = (long)shifts[j] - ((long)tasks[iIdx] - cur);
                if (t >= s[m] - s[iIdx + 1]) {
                    iIdx = 0;
                    cur = 0;
                } else {
                    int l = iIdx + 1, r = m;
                    while (l < r) {
                        int mid = (l + r) >> 1;
                        if (t < s[mid + 1] - s[iIdx + 1]) r = mid;
                        else l = mid + 1;
                    }
                    cur = t - (s[l] - s[iIdx + 1]);
                    iIdx = l;
                    ans[j] = m - iIdx;
                }
            }
        }
        return ans;
    }
}

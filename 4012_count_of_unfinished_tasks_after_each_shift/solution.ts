// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

export function countTasks(tasks: any, shifts: any): any {
        let m = tasks.length, n = shifts.length;
        let s = new Array(m + 1).fill(0);
        for (let i = 0; i < m; i++) s[i + 1] = s[i] + tasks[i];
        let ans = new Array(n).fill(0);
        let iIdx = 0;
        let cur = 0;
        for (let j = 0; j < n; j++) {
            if (shifts[j] < tasks[iIdx] - cur) {
                cur += shifts[j];
                ans[j] = m - iIdx;
            } else {
                let t = shifts[j] - (tasks[iIdx] - cur);
                if (t >= s[m] - s[iIdx + 1]) {
                    iIdx = 0;
                    cur = 0;
                } else {
                    let l = iIdx + 1, r = m;
                    while (l < r) {
                        let mid = (l + r) >> 1;
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

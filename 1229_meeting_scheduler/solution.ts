// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

function minAvailableDuration(slots1: number[][], slots2: number[][], duration: number): number[] {
    slots1.sort((a, b) => a[0] - b[0]);
    slots2.sort((a, b) => a[0] - b[0]);
    let i = 0, j = 0;
    while (i < slots1.length && j < slots2.length) {
        const start = Math.max(slots1[i][0], slots2[j][0]);
        const end = Math.min(slots1[i][1], slots2[j][1]);
        if (end - start >= duration) return [start, start + duration];
        if (slots1[i][1] < slots2[j][1]) i++;
        else j++;
    }
    return [];
}

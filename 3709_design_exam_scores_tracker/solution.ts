// LeetCode 3709 - Design Exam Scores Tracker
// https://leetcode.com/problems/design-exam-scores-tracker/

export class ExamTracker {
    constructor() {
    this.times = [0];
    this.pre = [0];
}
    record(time: any, score: any): any {
    this.times.push(time);
    this.pre.push(this.pre[this.pre.length - 1] + score);
}
    totalScore(startTime: any, endTime: any): any {
    const lowerBound = (a, target) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const l = lowerBound(this.times, startTime) - 1;
    const r = lowerBound(this.times, endTime + 1) - 1;
    return this.pre[r] - this.pre[l];
}
}

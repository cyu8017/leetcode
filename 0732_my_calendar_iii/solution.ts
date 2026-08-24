// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

export class MyCalendarThree {
    constructor() {
        this.delta = new Map();
    }

    book(startTime: any, endTime: any): any {
        this.delta.set(startTime, (this.delta.get(startTime) || 0) + 1);
        this.delta.set(endTime, (this.delta.get(endTime) || 0) - 1);
        let current = 0, best = 0;
        const keys = Array.from(this.delta.keys()).sort((a, b) => a - b);
        for (const key of keys) {
            current += this.delta.get(key);
            best = Math.max(best, current);
        }
        return best;
    }
}

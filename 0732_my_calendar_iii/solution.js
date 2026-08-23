// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree {
    constructor() {
        this.delta = new Map();
    }

    /**
     * @param {number} startTime
     * @param {number} endTime
     * @return {number}
     */
    book(startTime, endTime) {
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

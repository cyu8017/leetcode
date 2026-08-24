// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

export class MyCalendarTwo {
    constructor() {
        this.booked = [];
        this.overlaps = [];
    }

    book(startTime: any, endTime: any): any {
        for (const o of this.overlaps) {
            if (o[0] < endTime && startTime < o[1]) return false;
        }
        for (const b of this.booked) {
            if (b[0] < endTime && startTime < b[1]) {
                this.overlaps.push([Math.max(b[0], startTime), Math.min(b[1], endTime)]);
            }
        }
        this.booked.push([startTime, endTime]);
        return true;
    }
}

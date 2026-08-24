// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

export class MyCalendar {
    constructor() {
        this.bookings = [];
    }

    book(startTime: any, endTime: any): any {
        for (const b of this.bookings) {
            if (b[0] < endTime && startTime < b[1]) return false;
        }
        this.bookings.push([startTime, endTime]);
        return true;
    }
}

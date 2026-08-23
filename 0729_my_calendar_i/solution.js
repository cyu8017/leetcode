// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

class MyCalendar {
    constructor() {
        this.bookings = [];
    }

    /**
     * @param {number} startTime
     * @param {number} endTime
     * @return {boolean}
     */
    book(startTime, endTime) {
        for (const b of this.bookings) {
            if (b[0] < endTime && startTime < b[1]) return false;
        }
        this.bookings.push([startTime, endTime]);
        return true;
    }
}

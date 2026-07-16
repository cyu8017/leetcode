// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

export function canAttendMeetings(intervals: number[][]): boolean {
    intervals.sort((left, right) => left[0] - right[0]);
    for (let index = 1; index < intervals.length; index += 1) {
        if (intervals[index][0] < intervals[index - 1][1]) {
            return false;
        }
    }
    return true;
}

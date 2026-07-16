// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minMeetingRooms = function(intervals) {
    const starts = intervals.map(([start]) => start).sort((left, right) => left - right);
    const ends = intervals.map(([, end]) => end).sort((left, right) => left - right);
    let rooms = 0;
    let maxRooms = 0;
    let startIndex = 0;
    let endIndex = 0;

    while (startIndex < starts.length) {
        if (starts[startIndex] < ends[endIndex]) {
            rooms += 1;
            maxRooms = Math.max(maxRooms, rooms);
            startIndex += 1;
        } else {
            rooms -= 1;
            endIndex += 1;
        }
    }

    return maxRooms;
};

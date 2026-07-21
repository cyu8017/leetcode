"use strict";
// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/
function closestRoom(rooms, queries) {
    rooms = rooms.map((r) => [...r]).sort((a, b) => a[1] - b[1]);
    const indexedQueries = queries
        .map((q, i) => [i, q])
        .sort((a, b) => b[1][1] - a[1][1]);
    const availableIds = [];
    let roomIndex = rooms.length - 1;
    const answer = new Array(queries.length).fill(-1);
    const insort = (arr, val) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < val)
                lo = mid + 1;
            else
                hi = mid;
        }
        arr.splice(lo, 0, val);
    };
    const bisectLeft = (arr, val) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < val)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    };
    for (const [queryIndex, [preferred, minSize]] of indexedQueries) {
        while (roomIndex >= 0 && rooms[roomIndex][1] >= minSize) {
            insort(availableIds, rooms[roomIndex][0]);
            roomIndex -= 1;
        }
        if (availableIds.length === 0)
            continue;
        const pos = bisectLeft(availableIds, preferred);
        let bestId = -1;
        let bestDist = Infinity;
        if (pos < availableIds.length) {
            const roomId = availableIds[pos];
            const dist = Math.abs(roomId - preferred);
            if (dist < bestDist || (dist === bestDist && roomId < bestId)) {
                bestId = roomId;
                bestDist = dist;
            }
        }
        if (pos > 0) {
            const roomId = availableIds[pos - 1];
            const dist = Math.abs(roomId - preferred);
            if (dist < bestDist || (dist === bestDist && roomId < bestId)) {
                bestId = roomId;
                bestDist = dist;
            }
        }
        answer[queryIndex] = bestId;
    }
    return answer;
}

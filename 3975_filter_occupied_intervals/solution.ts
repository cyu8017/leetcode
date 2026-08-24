// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

export function filterOccupiedIntervals(occupiedIntervals: any, freeStart: any, freeEnd: any): any {
    occupiedIntervals.sort((a, b) => a[0] - b[0]);
    const busy = [];
    busy.push([occupiedIntervals[0][0], occupiedIntervals[0][1]]);
    for (let i = 1; i < occupiedIntervals.length; i++) {
        const cur = occupiedIntervals[i];
        const last = busy[busy.length - 1];
        if (last[1] + 1 < cur[0]) busy.push([cur[0], cur[1]]);
        else if (cur[1] > last[1]) last[1] = cur[1];
    }
    const ans = [];
    for (const it of busy) {
        const s = it[0], e = it[1];
        if (e < freeStart || s > freeEnd) ans.push([s, e]);
        else {
            if (s < freeStart) ans.push([s, freeStart - 1]);
            if (e > freeEnd) ans.push([freeEnd + 1, e]);
        }
    }
    return ans;
}

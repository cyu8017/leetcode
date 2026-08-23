// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var rectangleArea = function(rectangles) {
    const MOD = 1000000007;
    const events = [];
    for (const r of rectangles) {
        events.push([r[0], 1, r[1], r[3]]);
        events.push([r[2], -1, r[1], r[3]]);
    }
    events.sort((a, b) => a[0] - b[0]);
    const coveredLength = (active) => {
        if (!active.length) return 0;
        const sorted = active.slice().sort((a, b) => a[0] - b[0]);
        let total = 0, curStart = sorted[0][0], curEnd = sorted[0][1];
        for (let i = 1; i < sorted.length; i++) {
            const [start, end] = sorted[i];
            if (start > curEnd) {
                total += curEnd - curStart;
                curStart = start;
                curEnd = end;
            } else {
                curEnd = Math.max(curEnd, end);
            }
        }
        total += curEnd - curStart;
        return total;
    };
    const active = [];
    let area = 0;
    let prevX = events[0][0];
    for (const [x, typ, y1, y2] of events) {
        area += coveredLength(active) * (x - prevX);
        if (typ === 1) active.push([y1, y2]);
        else {
            for (let i = 0; i < active.length; i++) {
                if (active[i][0] === y1 && active[i][1] === y2) {
                    active.splice(i, 1);
                    break;
                }
            }
        }
        prevX = x;
    }
    return area % MOD;
};

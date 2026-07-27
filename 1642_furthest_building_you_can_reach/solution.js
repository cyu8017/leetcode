// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function(heights, bricks, ladders) {
    const climbs = [];
    const push = (x) => {
        climbs.push(x);
        let i = climbs.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (climbs[p] <= climbs[i]) break;
            [climbs[p], climbs[i]] = [climbs[i], climbs[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = climbs[0];
        const last = climbs.pop();
        if (!climbs.length) return top;
        climbs[0] = last;
        let i = 0;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < climbs.length && climbs[l] < climbs[s]) s = l;
            if (r < climbs.length && climbs[r] < climbs[s]) s = r;
            if (s === i) break;
            [climbs[s], climbs[i]] = [climbs[i], climbs[s]];
            i = s;
        }
        return top;
    };
    for (let i = 0; i < heights.length - 1; i++) {
        const d = heights[i + 1] - heights[i];
        if (d <= 0) continue;
        push(d);
        if (climbs.length > ladders) bricks -= pop();
        if (bricks < 0) return i;
    }
    return heights.length - 1;
};

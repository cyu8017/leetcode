// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

export function averageHeightOfBuildings(buildings: number[][]): number[][] {
    const events = [];
    for (const b of buildings) {
        events.push([b[0], 1, b[2]]);
        events.push([b[1], -1, b[2]]);
    }
    events.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    const ans = [];
    let count = 0, sum = 0, prev = events[0][0];
    for (const e of events) {
        if (e[0] !== prev && count > 0) {
            const avg = Math.floor(sum / count);
            if (ans.length && ans[ans.length - 1][1] === prev && ans[ans.length - 1][2] === avg)
                ans[ans.length - 1][1] = e[0];
            else ans.push([prev, e[0], avg]);
        }
        count += e[1];
        sum += e[1] * e[2];
        prev = e[0];
    }
    return ans;
}

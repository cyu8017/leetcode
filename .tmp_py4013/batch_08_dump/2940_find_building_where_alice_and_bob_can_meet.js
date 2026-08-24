// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

var leftmostBuildingQueries = function(heights, queries) {
    const qn = queries.length;
    const ans = new Array(qn).fill(-1);
    const buckets = Array.from({length: heights.length}, () => []);
    for (let qi = 0; qi < qn; qi++) {
        let a = queries[qi][0], b = queries[qi][1];
        if (a > b) { const t = a; a = b; b = t; }
        if (a === b || heights[a] < heights[b]) {
            ans[qi] = b;
            continue;
        }
        buckets[b].push([heights[a], qi]);
    }
    const st = [];
    for (let i = heights.length - 1; i >= 0; i--) {
        for (const p of buckets[i]) {
            const h = p[0], qi = p[1];
            let lo = 0, hi = st.length - 1, pos = -1;
            while (lo <= hi) {
                const mid = (lo + hi) >> 1;
                if (st[mid][0] > h) {
                    pos = st[mid][1];
                    lo = mid + 1;
                } else hi = mid - 1;
            }
            ans[qi] = pos;
        }
        while (st.length && st[st.length - 1][0] <= heights[i]) st.pop();
        st.push([heights[i], i]);
    }
    return ans;
};

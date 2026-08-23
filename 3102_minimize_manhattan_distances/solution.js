// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

/**
 * @param {number[][]} points
 * @return {number}
 */
var minimumDistance = function(points) {
    // multiset via Map + sorted keys
    const makeMS = () => {
        const m = new Map();
        const keys = [];
        const merge = (x, v) => {
            const nv = (m.get(x) || 0) + v;
            if (nv === 0) {
                m.delete(x);
                const i = keys.indexOf(x);
                if (i >= 0) keys.splice(i, 1);
            } else {
                if (!m.has(x)) {
                    let lo = 0, hi = keys.length;
                    while (lo < hi) {
                        const mid = (lo + hi) >> 1;
                        if (keys[mid] < x) lo = mid + 1;
                        else hi = mid;
                    }
                    keys.splice(lo, 0, x);
                }
                m.set(x, nv);
            }
        };
        return {
            merge,
            first: () => keys[0],
            last: () => keys[keys.length - 1],
        };
    };
    const st1 = makeMS(), st2 = makeMS();
    for (const p of points) {
        st1.merge(p[0] + p[1], 1);
        st2.merge(p[0] - p[1], 1);
    }
    let ans = Number.MAX_SAFE_INTEGER;
    for (const p of points) {
        const x = p[0], y = p[1];
        st1.merge(x + y, -1);
        st2.merge(x - y, -1);
        ans = Math.min(ans, Math.max(st1.last() - st1.first(), st2.last() - st2.first()));
        st1.merge(x + y, 1);
        st2.merge(x - y, 1);
    }
    return ans;
};

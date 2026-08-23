// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

var countTrapezoids = function(points) {
    const n = points.length;
    const cnt1 = new Map();
    const cnt2 = new Map();
    const getOr = (m, k) => {
        if (!m.has(k)) m.set(k, new Map());
        return m.get(k);
    };
    for (let i = 0; i < n; i++) {
        const x1 = points[i][0], y1 = points[i][1];
        for (let j = 0; j < i; j++) {
            const x2 = points[j][0], y2 = points[j][1];
            const dx = x2 - x1, dy = y2 - y1;
            let k, b;
            if (dx === 0) {
                k = 1e9;
                b = x1;
            } else {
                k = dy / dx;
                b = (y1 * dx - x1 * dy) / dx;
            }
            const m1 = getOr(cnt1, k);
            m1.set(b, (m1.get(b) || 0) + 1);
            const p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000);
            const m2 = getOr(cnt2, p);
            m2.set(k, (m2.get(k) || 0) + 1);
        }
    }
    let ans = 0;
    for (const e of cnt1.values()) {
        let s = 0;
        for (const t of e.values()) {
            ans += s * t;
            s += t;
        }
    }
    for (const e of cnt2.values()) {
        let s = 0;
        for (const t of e.values()) {
            ans -= s * t;
            s += t;
        }
    }
    return ans;
};

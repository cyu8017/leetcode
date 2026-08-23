// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

var maxActivated = function(points) {
    const p = new Map(), size = new Map();
    const find = (x) => {
        if (!p.has(x)) { p.set(x, x); size.set(x, 1); }
        if (p.get(x) !== x) p.set(x, find(p.get(x)));
        return p.get(x);
    };
    const unite = (a, b) => {
        let pa = find(a), pb = find(b);
        if (pa === pb) return false;
        if (size.get(pa) > size.get(pb)) {
            p.set(pb, pa);
            size.set(pa, size.get(pa) + size.get(pb));
        } else {
            p.set(pa, pb);
            size.set(pb, size.get(pb) + size.get(pa));
        }
        return true;
    };
    const m = 3000000000;
    for (const pt of points) unite(pt[0], pt[1] + m);
    const cnt = new Map();
    for (const pt of points) {
        const r = find(pt[0]);
        cnt.set(r, (cnt.get(r) || 0) + 1);
    }
    let mx1 = 0, mx2 = 0;
    for (const x of cnt.values()) {
        if (mx1 < x) { mx2 = mx1; mx1 = x; }
        else if (mx2 < x) mx2 = x;
    }
    return mx1 + mx2 + 1;
};

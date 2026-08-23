// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

function calc3588(coords) {
    let mn = 1e9, mx = 0;
    const f = new Map(), g = new Map();
    for (const c of coords) {
        const x = c[0], y = c[1];
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
        if (f.has(x)) {
            f.set(x, Math.min(f.get(x), y));
            g.set(x, Math.max(g.get(x), y));
        } else {
            f.set(x, y);
            g.set(x, y);
        }
    }
    let ans = 0;
    for (const [x, y] of f) {
        const d = g.get(x) - y;
        ans = Math.max(ans, d * Math.max(mx - x, x - mn));
    }
    return ans;
}
var maxArea = function(coords) {
    let ans = calc3588(coords);
    for (const c of coords) {
        const t = c[0];
        c[0] = c[1];
        c[1] = t;
    }
    ans = Math.max(ans, calc3588(coords));
    return ans > 0 ? ans : -1;
};

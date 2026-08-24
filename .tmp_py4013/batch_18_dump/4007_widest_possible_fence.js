// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

var maximumWidth = function(planks) {
    const cnt = new Map();
    for (const x of planks) cnt.set(x, (cnt.get(x) || 0) + 1);
    const t = new Map();
    let ans = 0;
    for (const [x, v1] of cnt.entries()) {
        t.set(x, (t.get(x) || 0) + v1);
        ans = Math.max(ans, t.get(x));
        t.set(x * 2, (t.get(x * 2) || 0) + Math.floor(v1 / 2));
        ans = Math.max(ans, t.get(x * 2));
        for (const [y, v2] of cnt.entries()) {
            if (y > x) {
                const key = x + y;
                t.set(key, (t.get(key) || 0) + Math.min(v1, v2));
                ans = Math.max(ans, t.get(key));
            }
        }
    }
    return ans;
};

// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

export function minimumString(a: string, b: string, c: string): string {
    const merge = (x, y) => {
        if (x.includes(y)) return x;
        let best = x + y;
        const n = Math.min(x.length, y.length);
        for (let i = n; i > 0; i--) {
            if (x.slice(-i) === y.slice(0, i)) {
                const cand = x + y.slice(i);
                if (cand.length < best.length || (cand.length === best.length && cand < best)) best = cand;
                break;
            }
        }
        return best;
    };
    const perms = [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]];
    let ans = '';
    for (const p of perms) {
        const cur = merge(merge(p[0], p[1]), p[2]);
        if (!ans || cur.length < ans.length || (cur.length === ans.length && cur < ans)) ans = cur;
    }
    return ans;
}

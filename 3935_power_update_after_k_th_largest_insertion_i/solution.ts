// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

function merge(st: any, x: any, v: any): any {
    const c = st.get(x) || 0;
    if (c + v === 0) st.delete(x);
    else st.set(x, c + v);
}function firstKey(st: any): any {
    let best = null;
    for (const k of st.keys()) if (best === null || k < best) best = k;
    return best;
}function lastKey(st: any): any {
    let best = null;
    for (const k of st.keys()) if (best === null || k > best) best = k;
    return best;
}function qpow(a: any, b: any, mod: any): any {
    let ans = 1;
    a = Number(a);
    while (b > 0) {
        if ((b & 1) !== 0) ans = Number((BigInt(ans) * BigInt(a)) % BigInt(mod));
        a = Number((BigInt(a) * BigInt(a)) % BigInt(mod));
        b >>= 1;
    }
    return ans;
}export function powerUpdate(nums: any, p: any, queries: any): any {
    const L = new Map(), R = new Map();
    let sz1 = 0, sz2 = nums.length;
    for (const x of nums) merge(R, x, 1);
    const mod = 1000000007;
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const val = queries[qi][0], k = queries[qi][1];
        merge(R, val, 1);
        sz2++;
        let node = firstKey(R);
        merge(R, node, -1);
        sz2--;
        merge(L, node, 1);
        sz1++;
        while (sz2 < k) {
            node = lastKey(L);
            merge(L, node, -1);
            sz1--;
            merge(R, node, 1);
            sz2++;
        }
        while (sz2 > k) {
            node = firstKey(R);
            merge(R, node, -1);
            sz2--;
            merge(L, node, 1);
            sz1++;
        }
        const x = firstKey(R);
        p = qpow(p, x, mod);
        ans[qi] = p;
    }
    return ans;
}

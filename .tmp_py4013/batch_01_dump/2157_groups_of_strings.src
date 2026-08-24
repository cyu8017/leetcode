// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

/**
 * @param {string[]} words
 * @return {number[]}
 */
var groupStrings = function(words) {
    const parent = new Map();
    const size = new Map();
    const find = (x) => {
        if (parent.get(x) !== x) parent.set(x, find(parent.get(x)));
        return parent.get(x);
    };
    const unite = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        if (size.get(ra) < size.get(rb)) { const t = ra; ra = rb; rb = t; }
        parent.set(rb, ra);
        size.set(ra, size.get(ra) + size.get(rb));
    };
    const maskOf = (w) => {
        let m = 0;
        for (let i = 0; i < w.length; i++) m |= 1 << (w.charCodeAt(i) - 97);
        return m;
    };
    const freq = new Map();
    for (const w of words) {
        const m = maskOf(w);
        freq.set(m, (freq.get(m) || 0) + 1);
    }
    for (const [k, v] of freq) {
        parent.set(k, k);
        size.set(k, v);
    }
    for (const m of [...freq.keys()]) {
        for (let b = 0; b < 26; b++) {
            if ((m & (1 << b)) !== 0) {
                const nm = m ^ (1 << b);
                if (freq.has(nm)) unite(m, nm);
                for (let a = 0; a < 26; a++) {
                    if ((nm & (1 << a)) === 0) {
                        const rm = nm | (1 << a);
                        if (freq.has(rm)) unite(m, rm);
                    }
                }
            } else {
                const nm = m | (1 << b);
                if (freq.has(nm)) unite(m, nm);
            }
        }
    }
    let groups = 0, maxSize = 0;
    const seen = new Set();
    for (const m of freq.keys()) {
        const r = find(m);
        if (!seen.has(r)) {
            seen.add(r);
            groups++;
            maxSize = Math.max(maxSize, size.get(r));
        }
    }
    return [groups, maxSize];
};

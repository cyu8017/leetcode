// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

export function longestRepeating(s_: string, queryCharacters: string, queryIndices: number[]): number[] {
    function merge(a: any, b: any): any {
        if (!a || a.size === 0) return b;
        if (!b || b.size === 0) return a;
        const res = { lChar: a.lChar, rChar: b.rChar, size: a.size + b.size, best: Math.max(a.best, b.best), lLen: a.lLen, rLen: b.rLen };
        if (a.rChar === b.lChar) {
            const mid = a.rLen + b.lLen;
            res.best = Math.max(res.best, mid);
            if (a.lLen === a.size) res.lLen = a.size + b.lLen;
            if (b.rLen === b.size) res.rLen = b.size + a.rLen;
        }
        return res;
    }    const s = s_.split('');
    const n = s.length;
    const tree = new Array(4 * n + 5);
    function build(idx: any, l: any, r: any): any {
        if (l === r) {
            tree[idx] = { lChar: s[l], rChar: s[l], lLen: 1, rLen: 1, best: 1, size: 1 };
            return;
        }
        const mid = (l + r) >> 1;
        build(idx * 2, l, mid);
        build(idx * 2 + 1, mid + 1, r);
        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }    function update(idx: any, l: any, r: any, pos: any, ch: any): any {
        if (l === r) {
            s[pos] = ch;
            tree[idx] = { lChar: ch, rChar: ch, lLen: 1, rLen: 1, best: 1, size: 1 };
            return;
        }
        const mid = (l + r) >> 1;
        if (pos <= mid) update(idx * 2, l, mid, pos, ch);
        else update(idx * 2 + 1, mid + 1, r, pos, ch);
        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }    build(1, 0, n - 1);
    const ans = new Array(queryIndices.length);
    for (let i = 0; i < queryIndices.length; i++) {
        update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
        ans[i] = tree[1].best;
    }
    return ans;
}

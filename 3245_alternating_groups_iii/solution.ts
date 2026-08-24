// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

export class SegTree {
    constructor(n_: any) {
        this.n = n_;
        this.treeIntervalCounts = new Array(4 * n_).fill(0);
        this.treeIntervalLengths = new Array(4 * n_).fill(0);
    }
    add(i: any, val: any): any { this.addRec(0, 0, this.n - 1, i, val); }
    addRec(treeIndex: any, lo: any, hi: any, i: any, val: any): any {
        if (lo === hi) {
            this.treeIntervalCounts[treeIndex] += val;
            this.treeIntervalLengths[treeIndex] = this.treeIntervalCounts[treeIndex] * i;
            return;
        }
        const mid = (lo + hi) >> 1;
        if (i <= mid) this.addRec(2 * treeIndex + 1, lo, mid, i, val);
        else this.addRec(2 * treeIndex + 2, mid + 1, hi, i, val);
        this.treeIntervalCounts[treeIndex] = this.treeIntervalCounts[2 * treeIndex + 1] + this.treeIntervalCounts[2 * treeIndex + 2];
        this.treeIntervalLengths[treeIndex] = this.treeIntervalLengths[2 * treeIndex + 1] + this.treeIntervalLengths[2 * treeIndex + 2];
    }
    queryIntervalCounts(i: any): any { return this.query(this.treeIntervalCounts, 0, 0, this.n - 1, i, this.n - 1); }
    queryIntervalLengths(i: any): any { return this.query(this.treeIntervalLengths, 0, 0, this.n - 1, i, this.n - 1); }
    query(tree: any, treeIndex: any, lo: any, hi: any, i: any, j: any): any {
        if (i <= lo && hi <= j) return tree[treeIndex];
        if (j < lo || hi < i) return 0;
        const mid = (lo + hi) >> 1;
        return this.query(tree, treeIndex * 2 + 1, lo, mid, i, j) + this.query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j);
    }
}

export function numberOfAlternatingGroups(colors: any, queries: any): any {
    const n = colors.length;
    const ans = [];
    const arr = new Array(2 * n - 1);
    for (let i = 0; i < n; i++) arr[i] = colors[i];
    for (let i = 0; i < n - 1; i++) arr[n + i] = colors[i];
    
    
    
    
    
    
    const pack = (l, r) => (BigInt(l) << 32n) | BigInt(r >>> 0);
    const unpackL = (v) => Number(v >> 32n);
    const unpackR = (v) => Number(v & 0xffffffffn);
    const tree = new SegTree(2 * n - 1);
    const intervals = new Set();
    const insert = (l, r) => {
        intervals.add(pack(l, r));
        if (l < n) tree.add(r - l + 1, 1);
    };
    const remove = (l, r) => {
        intervals.delete(pack(l, r));
        if (l < n) tree.add(r - l + 1, -1);
    };
    const findInterval = (target) => {
        let bestL = -1, bestR = -1;
        for (const k of intervals) {
            const kl = unpackL(k), kr = unpackR(k);
            if (kl <= target && target <= kr && kl > bestL) { bestL = kl; bestR = kr; }
        }
        return [bestL, bestR];
    };
    const getNum = (sz) => {
        const numIntervals = tree.queryIntervalCounts(sz);
        const sumIntervals = tree.queryIntervalLengths(sz);
        let numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals;
        const [l, r] = findInterval(n);
        if (l < 0 || l >= n || r - l + 1 < sz) return numAlternatingGroups;
        if (r >= n) {
            const nonDuplicateGroups = n - l;
            const numGroups = (r - l + 1) - sz + 1;
            const extra = numGroups - nonDuplicateGroups;
            if (extra > 0) numAlternatingGroups -= extra;
        }
        return numAlternatingGroups;
    };
    const update = (index, color) => {
        if (arr[index] === color) return;
        arr[index] = color;
        let [start, end] = findInterval(index);
        remove(start, end);
        if (start < index && index < end) {
            insert(start, index - 1);
            insert(index, index);
            insert(index + 1, end);
            return;
        }
        if (start === index && index < end) insert(start + 1, end);
        if (start < index && index === end) insert(start, end - 1);
        let ns = index, ne = index;
        for (;;) {
            let merged = false;
            for (const k of [...intervals]) {
                const kl = unpackL(k), kr = unpackR(k);
                if (kr + 1 === ns && arr[kr] !== arr[ns]) {
                    remove(kl, kr); ns = kl; merged = true; break;
                }
            }
            if (!merged) break;
        }
        for (;;) {
            let merged = false;
            for (const k of [...intervals]) {
                const kl = unpackL(k), kr = unpackR(k);
                if (kl === ne + 1 && arr[kl] !== arr[ne]) {
                    remove(kl, kr); ne = kr; merged = true; break;
                }
            }
            if (!merged) break;
        }
        insert(ns, ne);
    };
    let st = 0;
    for (let i = 1; i < 2 * n - 1; i++) {
        if (arr[i] === arr[i - 1]) { insert(st, i - 1); st = i; }
    }
    insert(st, 2 * n - 2);
    for (const query of queries) {
        if (query[0] === 1) ans.push(getNum(query[1]));
        else {
            const index = query[1], color = query[2];
            if (arr[index] !== color) {
                update(index, color);
                if (index < n - 1) update(index + n, color);
            }
        }
    }
    return ans;
}

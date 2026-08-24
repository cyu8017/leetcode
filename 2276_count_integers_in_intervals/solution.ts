// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

export class CountIntervals {
    constructor() {
    this.root = null;
    this.cnt = 0;
}
    add(left: any, right: any): any {
    const self = this;
    const addRange = (L, R, l, r, node) => {
        if (!node) node = { left: null, right: null, covered: false };
        if (node.covered) return [0, node];
        if (l <= L && R <= r) {
            node.covered = true;
            node.left = node.right = null;
            return [R - L + 1, node];
        }
        const mid = Math.floor((L + R) / 2);
        let added = 0;
        if (l <= mid) {
            const res = addRange(L, mid, l, r, node.left);
            added += res[0];
            node.left = res[1];
        }
        if (r > mid) {
            const res = addRange(mid + 1, R, l, r, node.right);
            added += res[0];
            node.right = res[1];
        }
        if (node.left && node.right && node.left.covered && node.right.covered) {
            node.covered = true;
            node.left = node.right = null;
        }
        return [added, node];
    };
    const res = addRange(1, 1000000000, left, right, this.root);
    this.cnt += res[0];
    this.root = res[1];
}
    count(): any {
    return this.cnt;
}
}

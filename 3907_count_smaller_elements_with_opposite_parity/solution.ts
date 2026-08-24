// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

export class BIT3907 {
    constructor(n_: any) {
    this.n = n_;
    this.c = new Array(n_ + 1).fill(0);
}
    update(x: any, delta: any): any {
    for (; x <= this.n; x += x & -x) this.c[x] += delta;
}
    query(x: any): any {
    let s = 0;
    for (; x > 0; x -= x & -x) s += this.c[x];
    return s;
}
}

export function countSmallerOppositeParity(nums: any): any {
    const n = nums.length;
    let sorted = nums.slice().sort((a, b) => a - b);
    let m = 0;
    for (let i = 0; i < sorted.length; i++) {
        if (i === 0 || sorted[i] !== sorted[i - 1]) sorted[m++] = sorted[i];
    }
    sorted = sorted.slice(0, m);
    const bits = [new BIT3907(m), new BIT3907(m)];
    const ans = new Array(n);
    for (let i = n - 1; i >= 0; i--) {
        let lo = 0, hi = sorted.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (sorted[mid] < nums[i]) lo = mid + 1;
            else hi = mid;
        }
        let x = lo + 1;
        ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1);
        bits[nums[i] & 1].update(x, 1);
    }
    return ans;
}

// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

export function minDeletions(s: any, queries: any): any {
    class BIT {
        constructor(n_) { this.n = n_; this.c = new Array(n_ + 1).fill(0); }
        update(x, delta) {
            for (; x <= this.n; x += x & -x) this.c[x] += delta;
        }
        query(x) {
            let s = 0;
            for (; x > 0; x -= x & -x) s += this.c[x];
            return s;
        }
    }
    const n = s.length;
    const nums = new Array(n).fill(0);
    const bit = new BIT(n);
    for (let i = 1; i < n; i++) {
        if (s[i] === s[i - 1]) {
            nums[i] = 1;
            bit.update(i + 1, 1);
        }
    }
    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const j = q[1];
            let delta = (nums[j] ^ 1) - nums[j];
            nums[j] ^= 1;
            bit.update(j + 1, delta);
            if (j + 1 < n) {
                delta = (nums[j + 1] ^ 1) - nums[j + 1];
                nums[j + 1] ^= 1;
                bit.update(j + 2, delta);
            }
        } else {
            const l = q[1], r = q[2];
            ans.push(bit.query(r + 1) - bit.query(l + 1));
        }
    }
    return ans;
}

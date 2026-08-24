// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

export class BIT {
    constructor(n: any) {
        this.n = n;
        this.c = new Array(n + 1).fill(0);
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

export function countOfPeaks(nums: any, queries: any): any {
    
    
    
    const n = nums.length;
    const tree = new BIT(n - 1);
    const updatePeak = (i, val) => {
        if (i <= 0 || i >= n - 1) return;
        if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) tree.update(i, val);
    };
    for (let i = 1; i < n - 1; i++) updatePeak(i, 1);
    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const l = q[1] + 1, r = q[2] - 1;
            let t = 0;
            if (l <= r) t = tree.query(r) - tree.query(l - 1);
            ans.push(t);
        } else {
            const idx = q[1], val = q[2];
            for (let i = idx - 1; i <= idx + 1; i++) updatePeak(i, -1);
            nums[idx] = val;
            for (let i = idx - 1; i <= idx + 1; i++) updatePeak(i, 1);
        }
    }
    return ans;
}

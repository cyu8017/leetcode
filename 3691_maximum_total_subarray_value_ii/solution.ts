// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

export function maxTotalValue(nums: any, k: any): any {
    class SparseTableRMQ {
        constructor(data) {
            this.n = data.length;
            let maxLog = 0;
            while ((1 << maxLog) <= this.n) maxLog++;
            maxLog++;
            this.fMax = Array.from({length: this.n}, () => new Array(maxLog).fill(0));
            this.fMin = Array.from({length: this.n}, () => new Array(maxLog).fill(0));
            this.lg = new Array(this.n + 1).fill(0);
            for (let i = 2; i <= this.n; i++) this.lg[i] = this.lg[i >> 1] + 1;
            for (let i = 0; i < this.n; i++) {
                this.fMax[i][0] = data[i];
                this.fMin[i][0] = data[i];
            }
            for (let j = 1; j < maxLog; j++) {
                for (let i = 0; i <= this.n - (1 << j); i++) {
                    this.fMax[i][j] = Math.max(this.fMax[i][j - 1], this.fMax[i + (1 << (j - 1))][j - 1]);
                    this.fMin[i][j] = Math.min(this.fMin[i][j - 1], this.fMin[i + (1 << (j - 1))][j - 1]);
                }
            }
        }
        queryMax(l, r) {
            const k = this.lg[r - l + 1];
            return Math.max(this.fMax[l][k], this.fMax[r - (1 << k) + 1][k]);
        }
        queryMin(l, r) {
            const k = this.lg[r - l + 1];
            return Math.min(this.fMin[l][k], this.fMin[r - (1 << k) + 1][k]);
        }
    }
    const n = nums.length;
    const st = new SparseTableRMQ(nums);
    const pq = [];
    for (let l = 0; l < n; l++) {
        const val = st.queryMax(l, n - 1) - st.queryMin(l, n - 1);
        pq.push([val, l, n - 1]);
    }
    pq.sort((a, b) => b[0] - a[0]);
    let ans = 0;
    for (let i = 0; i < k; i++) {
        const top = pq.shift();
        const val = top[0], l = top[1], r = top[2];
        ans += val;
        if (r > l) {
            const nextVal = st.queryMax(l, r - 1) - st.queryMin(l, r - 1);
            pq.push([nextVal, l, r - 1]);
            pq.sort((a, b) => b[0] - a[0]);
        }
    }
    return ans;
}

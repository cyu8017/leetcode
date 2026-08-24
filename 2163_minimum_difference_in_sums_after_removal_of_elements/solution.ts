// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

export function minimumDifference(nums: number[]): number {
    const n = Math.floor(nums.length / 3);
    const left = new Array(nums.length).fill(0);
    const right = new Array(nums.length).fill(0);
    // max-heap as min-heap of negated values
    const hmax = [];
    const pushMax = (x) => {
        hmax.push(x);
        let i = hmax.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (hmax[p] >= hmax[i]) break;
            [hmax[p], hmax[i]] = [hmax[i], hmax[p]];
            i = p;
        }
    };
    const popMax = () => {
        const top = hmax[0];
        const last = hmax.pop();
        if (hmax.length) {
            hmax[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < hmax.length && hmax[l] > hmax[s]) s = l;
                if (r < hmax.length && hmax[r] > hmax[s]) s = r;
                if (s === i) break;
                [hmax[s], hmax[i]] = [hmax[i], hmax[s]];
                i = s;
            }
        }
        return top;
    };
    let sum = 0;
    for (let i = 0; i < n; i++) { pushMax(nums[i]); sum += nums[i]; }
    left[n - 1] = sum;
    for (let i = n; i < 2 * n; i++) {
        pushMax(nums[i]);
        sum += nums[i];
        sum -= popMax();
        left[i] = sum;
    }
    const hmin = [];
    const pushMin = (x) => {
        hmin.push(x);
        let i = hmin.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (hmin[p] <= hmin[i]) break;
            [hmin[p], hmin[i]] = [hmin[i], hmin[p]];
            i = p;
        }
    };
    const popMin = () => {
        const top = hmin[0];
        const last = hmin.pop();
        if (hmin.length) {
            hmin[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < hmin.length && hmin[l] < hmin[s]) s = l;
                if (r < hmin.length && hmin[r] < hmin[s]) s = r;
                if (s === i) break;
                [hmin[s], hmin[i]] = [hmin[i], hmin[s]];
                i = s;
            }
        }
        return top;
    };
    sum = 0;
    for (let i = nums.length - 1; i >= 2 * n; i--) { pushMin(nums[i]); sum += nums[i]; }
    right[2 * n] = sum;
    for (let i = 2 * n - 1; i >= n; i--) {
        pushMin(nums[i]);
        sum += nums[i];
        sum -= popMin();
        right[i] = sum;
    }
    let ans = left[n - 1] - right[n];
    for (let i = n; i < 2 * n; i++) ans = Math.min(ans, left[i] - right[i + 1]);
    return ans;
}

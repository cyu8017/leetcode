// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

function minimumDeviation(nums: number[]): number {
    const h: number[] = [];
    const push = (x: number): void => {
        h.push(x);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (h[p] >= h[i]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    };
    const pop = (): number => {
        const top = h[0];
        const last = h.pop()!;
        if (!h.length) return top;
        h[0] = last;
        let i = 0;
        const n = h.length;
        while (true) {
            let largest = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < n && h[l] > h[largest]) largest = l;
            if (r < n && h[r] > h[largest]) largest = r;
            if (largest === i) break;
            [h[i], h[largest]] = [h[largest], h[i]];
            i = largest;
        }
        return top;
    };
    let mn = Infinity;
    for (let x of nums) {
        if (x % 2) x *= 2;
        mn = Math.min(mn, x);
        push(x);
    }
    let ans = Infinity;
    while (true) {
        const x = pop();
        ans = Math.min(ans, x - mn);
        if (x % 2) return ans;
        const nx = x / 2;
        mn = Math.min(mn, nx);
        push(nx);
    }
}

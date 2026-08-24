// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

export function minJumps(nums: any): any {
    const MX = 1000001;
    if (!minJumps._factors) {
        const factors = Array.from({length: MX}, () => []);
        for (let i = 2; i < MX; i++) {
            if (factors[i].length === 0) {
                for (let j = i; j < MX; j += i) factors[j].push(i);
            }
        }
        minJumps._factors = factors;
    }
    const fac = minJumps._factors;
    const n = nums.length;
    const g = new Map();
    for (let i = 0; i < n; i++) {
        for (const p of fac[nums[i]]) {
            if (!g.has(p)) g.set(p, []);
            g.get(p).push(i);
        }
    }
    let ans = 0;
    const vis = new Array(n).fill(false);
    vis[0] = true;
    let q = [0];
    while (true) {
        const nq = [];
        for (const i of q) {
            if (i === n - 1) return ans;
            const idx = (g.get(nums[i]) || []).slice();
            idx.push(i + 1);
            if (i > 0) idx.push(i - 1);
            for (const j of idx) {
                if (j >= 0 && j < n && !vis[j]) {
                    vis[j] = true;
                    nq.push(j);
                }
            }
            g.set(nums[i], []);
        }
        q = nq;
        ans++;
    }
}

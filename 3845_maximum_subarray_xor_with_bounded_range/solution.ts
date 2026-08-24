// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

export function maxSubarrayXor(nums: any, k: any): any {
    const nodes = [{ next: [0, 0], count: 0 }];
    const add = (x, delta) => {
        let u = 0;
        nodes[u].count += delta;
        for (let b = 15; b >= 0; b--) {
            const bit = (x >> b) & 1;
            if (nodes[u].next[bit] === 0) {
                nodes[u].next[bit] = nodes.length;
                nodes.push({ next: [0, 0], count: 0 });
            }
            u = nodes[u].next[bit];
            nodes[u].count += delta;
        }
    };
    const query = (x) => {
        let u = 0, res = 0;
        for (let b = 15; b >= 0; b--) {
            const bit = (x >> b) & 1;
            const want = bit ^ 1;
            const v = nodes[u].next[want];
            if (v !== 0 && nodes[v].count > 0) {
                res |= 1 << b;
                u = v;
            } else {
                u = nodes[u].next[bit];
            }
        }
        return res;
    };
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] ^ nums[i];
    const maxQ = [], minQ = [];
    let left = 0, trieLeft = 0, ans = 0;
    for (let r = 0; r < n; r++) {
        const x = nums[r];
        while (maxQ.length && nums[maxQ[maxQ.length - 1]] <= x) maxQ.pop();
        maxQ.push(r);
        while (minQ.length && nums[minQ[minQ.length - 1]] >= x) minQ.pop();
        minQ.push(r);
        while (nums[maxQ[0]] - nums[minQ[0]] > k) {
            if (maxQ[0] === left) maxQ.shift();
            if (minQ[0] === left) minQ.shift();
            left++;
        }
        add(pref[r], 1);
        while (trieLeft < left) {
            add(pref[trieLeft], -1);
            trieLeft++;
        }
        const cur = query(pref[r + 1]);
        if (cur > ans) ans = cur;
    }
    return ans;
}

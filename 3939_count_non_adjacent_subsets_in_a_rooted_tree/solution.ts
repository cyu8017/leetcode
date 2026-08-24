// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

export function countNonAdjacentSubsets(parent: any, nums: any, k: any): any {
    const mod = 1000000007;
    const n = parent.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) children[parent[i]].push(i);
    const dp0 = new Array(n);
    const dp1 = new Array(n);
    for (let u = n - 1; u >= 0; u--) {
        let a = new Array(k).fill(0), b = new Array(k).fill(0);
        a[0] = 1;
        b[(((nums[u] % k) + k) % k)] = 1;
        for (const v of children[u]) {
            const na = new Array(k).fill(0), nb = new Array(k).fill(0);
            for (let x = 0; x < k; x++) {
                for (let y = 0; y < k; y++) {
                    const allChild = (dp0[v][y] + dp1[v][y]) % mod;
                    na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % mod;
                    nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % mod;
                }
            }
            a = na;
            b = nb;
        }
        dp0[u] = a;
        dp1[u] = b;
    }
    let ans = (dp0[0][0] + dp1[0][0] - 1) % mod;
    if (ans < 0) ans += mod;
    return ans;
}

// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

/**
 * @param {number[]} prevRoom
 * @return {number}
 */
var waysToBuildRooms = function(prevRoom) {
    const MOD = 1000000007;
    const n = prevRoom.length;
    const children = Array.from({ length: n }, () => []);
    for (let room = 0; room < n; room++) {
        if (prevRoom[room] !== -1) children[prevRoom[room]].push(room);
    }
    const fact = new Array(n + 1).fill(1);
    const invFact = new Array(n + 1).fill(1);
    for (let i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
    const modPow = (a, e) => {
        let r = 1n, base = BigInt(a), exp = BigInt(e), mod = BigInt(MOD);
        while (exp > 0n) {
            if (exp & 1n) r = r * base % mod;
            base = base * base % mod;
            exp >>= 1n;
        }
        return Number(r);
    };
    invFact[n] = modPow(fact[n], MOD - 2);
    for (let i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    const comb = (a, b) => fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
    const dfs = (node) => {
        let size = 0, ways = 1;
        for (const child of children[node]) {
            const [childSize, childWays] = dfs(child);
            ways = ways * childWays % MOD * comb(size + childSize, childSize) % MOD;
            size += childSize;
        }
        return [size + 1, ways];
    };
    return dfs(0)[1];
};

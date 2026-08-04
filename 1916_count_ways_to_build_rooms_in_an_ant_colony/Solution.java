// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

import java.util.*;

class Solution {
    static final int MOD = 1_000_000_007;
    long[] fact, invFact;
    List<Integer>[] children;

    public int waysToBuildRooms(int[] prevRoom) {
        int n = prevRoom.length;
        children = new ArrayList[n];
        for (int i = 0; i < n; i++) children[i] = new ArrayList<>();
        for (int room = 0; room < n; room++) {
            if (prevRoom[room] != -1) children[prevRoom[room]].add(room);
        }
        fact = new long[n + 1];
        invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        return (int) dfs(0)[1];
    }

    private long[] dfs(int node) {
        long size = 0, ways = 1;
        for (int child : children[node]) {
            long[] res = dfs(child);
            long childSize = res[0], childWays = res[1];
            ways = ways * childWays % MOD * comb(size + childSize, childSize) % MOD;
            size += childSize;
        }
        return new long[]{size + 1, ways};
    }

    private long comb(long a, long b) {
        return fact[(int) a] * invFact[(int) b] % MOD * invFact[(int) (a - b)] % MOD;
    }

    private long modPow(long a, long e) {
        long r = 1;
        while (e > 0) {
            if ((e & 1) == 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
}

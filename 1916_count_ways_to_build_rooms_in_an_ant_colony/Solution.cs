// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

using System.Collections.Generic;

public class Solution {
    const int MOD = 1000000007;
    long[] fact, invFact;
    List<int>[] children;

    public int WaysToBuildRooms(int[] prevRoom) {
        int n = prevRoom.Length;
        children = new List<int>[n];
        for (int i = 0; i < n; i++) children[i] = new List<int>();
        for (int room = 0; room < n; room++)
            if (prevRoom[room] != -1) children[prevRoom[room]].Add(room);

        fact = new long[n + 1];
        invFact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = ModPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;

        return (int)Dfs(0).ways;
    }

    long Comb(int a, int b) => fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;

    long ModPow(long x, long e) {
        long r = 1;
        while (e > 0) {
            if ((e & 1) == 1) r = r * x % MOD;
            x = x * x % MOD;
            e >>= 1;
        }
        return r;
    }

    (int size, long ways) Dfs(int node) {
        int size = 0;
        long ways = 1;
        foreach (int child in children[node]) {
            var (cs, cw) = Dfs(child);
            ways = ways * cw % MOD * Comb(size + cs, cs) % MOD;
            size += cs;
        }
        return (size + 1, ways);
    }
}
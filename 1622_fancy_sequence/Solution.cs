// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

using System.Collections.Generic;

public class Fancy {
    private const long MOD = 1000000007;
    private readonly List<long> vals = new();
    private long mul = 1;
    private long add = 0;

    public Fancy() {}

    public void Append(int val) {
        long inv = ModPow(mul, MOD - 2);
        vals.Add(((val - add) % MOD + MOD) % MOD * inv % MOD);
    }

    public void AddAll(int inc) {
        if (vals.Count > 0) add = (add + inc) % MOD;
    }

    public void MultAll(int m) {
        if (vals.Count == 0) return;
        mul = mul * m % MOD;
        add = add * m % MOD;
    }

    public int GetIndex(int idx) {
        if (idx >= vals.Count) return -1;
        return (int)((vals[idx] * mul + add) % MOD);
    }

    private static long ModPow(long baseVal, long exp) {
        long r = 1;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) r = r * baseVal % MOD;
            baseVal = baseVal * baseVal % MOD;
            exp >>= 1;
        }
        return r;
    }
}

// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

import java.util.*;

class Fancy {
    private static final long MOD = 1_000_000_007;
    private final List<Long> vals = new ArrayList<>();
    private long mul = 1;
    private long add = 0;

    public Fancy() {}

    public void append(int val) {
        long inv = modPow(mul, MOD - 2);
        long stored = ((val - add) % MOD + MOD) % MOD * inv % MOD;
        vals.add(stored);
    }

    public void addAll(int inc) {
        if (!vals.isEmpty()) add = (add + inc) % MOD;
    }

    public void multAll(int m) {
        if (vals.isEmpty()) return;
        mul = mul * m % MOD;
        add = add * m % MOD;
    }

    public int getIndex(int idx) {
        if (idx >= vals.size()) return -1;
        return (int) ((vals.get(idx) * mul + add) % MOD);
    }

    private long modPow(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
}

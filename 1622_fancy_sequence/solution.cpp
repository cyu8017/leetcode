// LeetCode 1622 - Fancy Sequence
// https://leetcode.com/problems/fancy-sequence/

#include <vector>

class Fancy {
    static constexpr long long MOD = 1000000007;
    std::vector<long long> vals_;
    long long mul_ = 1;
    long long add_ = 0;

    static long long modPow(long long base, long long exp) {
        long long r = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp & 1) {
                r = r * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }
        return r;
    }

public:
    Fancy() = default;

    void append(int val) {
        const long long inv = modPow(mul_, MOD - 2);
        vals_.push_back(((val - add_) % MOD + MOD) % MOD * inv % MOD);
    }

    void addAll(int inc) {
        if (!vals_.empty()) {
            add_ = (add_ + inc) % MOD;
        }
    }

    void multAll(int m) {
        if (vals_.empty()) {
            return;
        }
        mul_ = mul_ * m % MOD;
        add_ = add_ * m % MOD;
    }

    int getIndex(int idx) {
        if (idx >= static_cast<int>(vals_.size())) {
            return -1;
        }
        return static_cast<int>((vals_[idx] * mul_ + add_) % MOD);
    }
};

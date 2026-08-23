// LeetCode 3549 - Multiply Two Polynomials
// https://leetcode.com/problems/multiply-two-polynomials/

#include <vector>
#include <complex>
#include <cmath>
#include <algorithm>

class Solution {
    using cd = std::complex<double>;
    void fft(std::vector<cd>& a, bool invert) {
        int n = (int)a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) std::swap(a[i], a[j]);
        }
        for (int length = 2; length <= n; length <<= 1) {
            double angle = 2 * acos(-1.0) / length * (invert ? -1 : 1);
            cd wlen(cos(angle), sin(angle));
            for (int i = 0; i < n; i += length) {
                cd w(1);
                int half = length >> 1;
                for (int j = 0; j < half; j++) {
                    cd u = a[i + j];
                    cd v = a[i + j + half] * w;
                    a[i + j] = u + v;
                    a[i + j + half] = u - v;
                    w *= wlen;
                }
            }
        }
        if (invert) for (auto& x : a) x /= n;
    }
public:
    std::vector<long long> multiply(std::vector<int>& poly1, std::vector<int>& poly2) {
        if (poly1.empty() || poly2.empty()) return {};
        int m = (int)poly1.size() + (int)poly2.size() - 1;
        int n = 1;
        while (n < m) n <<= 1;
        std::vector<cd> fa(n), fb(n);
        for (int i = 0; i < (int)poly1.size(); i++) fa[i] = poly1[i];
        for (int i = 0; i < (int)poly2.size(); i++) fb[i] = poly2[i];
        fft(fa, false);
        fft(fb, false);
        for (int i = 0; i < n; i++) fa[i] *= fb[i];
        fft(fa, true);
        std::vector<long long> res(m);
        for (int i = 0; i < m; i++) res[i] = (long long)llround(fa[i].real());
        return res;
    }
};

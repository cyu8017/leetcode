// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

#include <algorithm>
#include <string>

class Solution {
public:
    bool isDigitorialPermutation(int n) {
        int f[10];
        f[0] = 1;
        for (int i = 1; i < 10; i++) f[i] = f[i - 1] * i;
        int x = 0, y = n;
        while (y > 0) {
            x += f[y % 10];
            y /= 10;
        }
        std::string a = std::to_string(x), b = std::to_string(n);
        std::sort(a.begin(), a.end());
        std::sort(b.begin(), b.end());
        return a == b;
    }
};

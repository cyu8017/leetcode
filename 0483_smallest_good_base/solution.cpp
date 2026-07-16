// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

#include <cmath>
#include <string>

class Solution {
public:
    std::string smallestGoodBase(std::string n) {
        const unsigned long long num = std::stoull(n);
        for (int length = static_cast<int>(std::log2(static_cast<long double>(num))) + 1; length >= 2;
             --length) {
            unsigned long long low = 2;
            unsigned long long high = num - 1;
            while (low <= high) {
                const unsigned long long mid = low + (high - low) / 2;
                __int128 total = 1;
                __int128 power = 1;
                bool ok = true;
                for (int i = 1; i < length; ++i) {
                    power *= mid;
                    total += power;
                    if (total > static_cast<__int128>(num)) {
                        ok = false;
                        break;
                    }
                }
                if (ok && total == static_cast<__int128>(num)) {
                    return std::to_string(mid);
                }
                if (!ok || total > static_cast<__int128>(num)) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        return std::to_string(num - 1);
    }
};

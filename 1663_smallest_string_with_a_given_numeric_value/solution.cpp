// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

#include <algorithm>
#include <string>

class Solution {
public:
    std::string getSmallestString(int n, int k) {
        std::string a(n, 'a');
        k -= n;
        for (int i = n - 1; i >= 0 && k > 0; --i) {
            int d = std::min(25, k);
            a[i] = static_cast<char>('a' + d);
            k -= d;
        }
        return a;
    }
};

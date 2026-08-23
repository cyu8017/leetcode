// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

#include <string>

class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int ans = 0;
        for (int x = low; x <= high; x++) {
            std::string s = std::to_string(x);
            if (s.size() % 2) continue;
            int mid = (int)s.size() / 2, a = 0, b = 0;
            for (int i = 0; i < mid; i++) {
                a += s[i] - '0';
                b += s[mid + i] - '0';
            }
            if (a == b) ans++;
        }
        return ans;
    }
};

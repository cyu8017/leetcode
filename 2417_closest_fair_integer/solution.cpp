// LeetCode 2417 - Closest Fair Integer
// https://leetcode.com/problems/closest-fair-integer/

#include <string>

class Solution {
public:
    int closestFair(int n) {
        for (int x = n; ; x++) {
            std::string s = std::to_string(x);
            if ((int)s.size() % 2 != 0) {
                int p = 1;
                for (int i = 0; i < (int)s.size(); i++) p *= 10;
                return closestFair(p);
            }
            int even = 0, odd = 0;
            for (char c : s) {
                if ((c - '0') % 2 == 0) even++;
                else odd++;
            }
            if (even == odd) return x;
        }
    }
};

// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    char kthCharacter(std::string s, long long k) {
        std::istringstream iss(s);
        std::string w;
        while (iss >> w) {
            long long m = (1 + (long long)w.size()) * (long long)w.size() / 2;
            if (k == m) return ' ';
            if (k > m) {
                k -= m + 1;
            } else {
                long long cur = 0;
                for (int i = 0;; i++) {
                    cur += i + 1;
                    if (k < cur) return w[i];
                }
            }
        }
        return ' ';
    }
};

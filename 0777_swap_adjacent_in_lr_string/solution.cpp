// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

#include <string>

class Solution {
public:
    bool canTransform(std::string start, std::string result) {
        std::string a;
        std::string b;
        for (char ch : start) {
            if (ch != 'X') {
                a.push_back(ch);
            }
        }
        for (char ch : result) {
            if (ch != 'X') {
                b.push_back(ch);
            }
        }
        if (a != b) {
            return false;
        }
        int i = 0;
        int j = 0;
        int n = static_cast<int>(start.size());
        while (i < n && j < n) {
            while (i < n && start[i] == 'X') {
                ++i;
            }
            while (j < n && result[j] == 'X') {
                ++j;
            }
            if (i == n || j == n) {
                break;
            }
            if (start[i] != result[j]) {
                return false;
            }
            if (start[i] == 'L' && i < j) {
                return false;
            }
            if (start[i] == 'R' && i > j) {
                return false;
            }
            ++i;
            ++j;
        }
        return true;
    }
};

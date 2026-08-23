// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

#include <string>
#include <vector>

class Solution {
public:
    std::string shiftingLetters(std::string s, std::vector<std::vector<int>>& shifts) {
        int n = (int)s.size();
        std::vector<int> diff(n + 1);
        for (auto& sh : shifts) {
            int d = sh[2] == 0 ? -1 : 1;
            diff[sh[0]] += d;
            diff[sh[1] + 1] -= d;
        }
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur = (cur + diff[i]) % 26;
            if (cur < 0) cur += 26;
            s[i] = char('a' + (s[i] - 'a' + cur) % 26);
        }
        return s;
    }
};

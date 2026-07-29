#include <string>
#include <vector>

class Solution {
public:
    std::string largestMultipleOfThree(std::vector<int>& digits) {
        int cnt[10] = {};
        int rem = 0;
        for (int d : digits) { ++cnt[d]; rem = (rem + d) % 3; }
        auto remove = [&](int r, int k) {
            for (int d = r; d < 10; d += 3) {
                while (cnt[d] && k) { --cnt[d]; --k; }
                if (!k) return true;
            }
            return false;
        };
        if (rem && !remove(rem, 1)) remove(3 - rem, 2);
        std::string s;
        for (int d = 9; d >= 0; --d) s += std::string(cnt[d], char('0' + d));
        if (!s.empty() && s[0] == '0') return "0";
        return s;
    }
};

// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> splitMessage(std::string message, int limit) {
        int n = (int)message.size();
        auto itoa = [](int x) {
            if (x == 0) return std::string("0");
            std::string b;
            while (x > 0) {
                b.insert(b.begin(), char('0' + x % 10));
                x /= 10;
            }
            return b;
        };
        for (int parts = 1; parts <= n; parts++) {
            int sbDigits = (int)itoa(parts).size();
            bool ok = true;
            int idx = 0;
            std::vector<std::string> res;
            res.reserve(parts);
            for (int i = 1; i <= parts; i++) {
                int tail = 3 + (int)itoa(i).size() + sbDigits;
                int cap = limit - tail;
                if (cap <= 0 || idx >= n) {
                    ok = false;
                    break;
                }
                int take = cap;
                if (take > n - idx) take = n - idx;
                res.push_back(message.substr(idx, take) + "<" + itoa(i) + "/" + itoa(parts) + ">");
                idx += take;
            }
            if (ok && idx == n) return res;
        }
        return {};
    }
};

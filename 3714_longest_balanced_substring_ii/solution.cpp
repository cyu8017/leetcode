// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <utility>

class Solution {
    int calc1(const std::string& s) {
        int res = 0, n = (int)s.size(), i = 0;
        while (i < n) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) j++;
            res = std::max(res, j - i);
            i = j;
        }
        return res;
    }

    int calc2(const std::string& s, char a, char b) {
        int res = 0, n = (int)s.size(), i = 0;
        while (i < n) {
            while (i < n && s[i] != a && s[i] != b) i++;
            std::unordered_map<int, int> pos{{0, i - 1}};
            int d = 0;
            while (i < n && (s[i] == a || s[i] == b)) {
                if (s[i] == a) d++;
                else d--;
                auto it = pos.find(d);
                if (it != pos.end()) res = std::max(res, i - it->second);
                else pos[d] = i;
                i++;
            }
        }
        return res;
    }

    int calc3(const std::string& s) {
        struct KeyHash {
            size_t operator()(const std::pair<int, int>& p) const {
                return (size_t)p.first * 1000003u + (size_t)p.second;
            }
        };
        std::unordered_map<std::pair<int, int>, int, KeyHash> pos;
        pos[{0, 0}] = -1;
        int cnt[3] = {}, res = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            cnt[s[i] - 'a']++;
            int x = cnt[0] - cnt[1], y = cnt[1] - cnt[2];
            auto k = std::make_pair(x, y);
            auto it = pos.find(k);
            if (it != pos.end()) res = std::max(res, i - it->second);
            else pos[k] = i;
        }
        return res;
    }

public:
    int longestBalanced(std::string s) {
        int x = calc1(s);
        int y = std::max({calc2(s, 'a', 'b'), calc2(s, 'b', 'c'), calc2(s, 'a', 'c')});
        int z = calc3(s);
        return std::max({x, y, z});
    }
};

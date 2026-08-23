// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int score(std::vector<std::string>& cards, char x) {
        int xx = 0;
        int left[26] = {}, right[26] = {};
        for (auto& c : cards) {
            char a = c[0], b = c[1];
            if (a == x && b == x) xx++;
            else if (a == x) left[b - 'a']++;
            else if (b == x) right[a - 'a']++;
        }
        auto pairGroup = [](int* arr) {
            int total = 0, mx = 0;
            for (int i = 0; i < 26; i++) {
                total += arr[i];
                mx = std::max(mx, arr[i]);
            }
            int pairs = total / 2;
            if (total - mx < pairs) pairs = total - mx;
            return std::make_pair(pairs, total - 2 * pairs);
        };
        auto [lp, lr] = pairGroup(left);
        auto [rp, rr] = pairGroup(right);
        int ans = lp + rp;
        int rem = lr + rr;
        int use = std::min(xx, rem);
        ans += use;
        xx -= use;
        ans += xx / 2;
        return ans;
    }
};

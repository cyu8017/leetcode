// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::string lexGreaterPermutation(std::string s, std::string target) {
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        int n = (int)s.size();
        std::string ans(n, ' ');
        std::function<bool(int, bool)> dfs = [&](int pos, bool greater) -> bool {
            if (pos == n) return greater;
            int start = greater ? 0 : (target[pos] - 'a');
            for (int c = start; c < 26; c++) {
                if (cnt[c] == 0) continue;
                cnt[c]--;
                ans[pos] = char('a' + c);
                bool ng = greater || c > (target[pos] - 'a');
                if (dfs(pos + 1, ng)) return true;
                cnt[c]++;
            }
            return false;
        };
        if (dfs(0, false)) return ans;
        return "";
    }
};

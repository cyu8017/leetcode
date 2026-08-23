// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string majorityFrequencyGroup(std::string s) {
        std::vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        std::unordered_map<int, std::string> f;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) f[cnt[i]].push_back(char('a' + i));
        }
        int mx = 0, mv = 0;
        std::string ans;
        for (auto& [v, cs] : f) {
            if ((int)cs.size() > mx || ((int)cs.size() == mx && v > mv)) {
                mx = (int)cs.size();
                mv = v;
                ans = cs;
            }
        }
        return ans;
    }
};

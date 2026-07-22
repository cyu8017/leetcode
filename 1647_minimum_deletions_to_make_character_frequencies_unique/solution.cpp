// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int minDeletions(std::string s) {
        std::unordered_map<char, int> freq;
        for (char c : s) {
            ++freq[c];
        }
        std::unordered_set<int> used;
        int ans = 0;
        for (auto [_, x] : freq) {
            while (x && used.count(x)) {
                --x;
                ++ans;
            }
            used.insert(x);
        }
        return ans;
    }
};

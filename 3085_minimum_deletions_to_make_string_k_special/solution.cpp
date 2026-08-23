// LeetCode 3085 - Minimum Deletions to Make String K-Special
// https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minimumDeletions(std::string word, int k) {
        int freq[26] = {};
        for (char c : word) freq[c - 'a']++;
        std::vector<int> nums;
        for (int v : freq) if (v > 0) nums.push_back(v);
        auto f = [&](int v) {
            int ans = 0;
            for (int x : nums) {
                if (x < v) ans += x;
                else if (x > v + k) ans += x - v - k;
            }
            return ans;
        };
        int ans = (int)word.size();
        for (int i = 0; i <= (int)word.size(); i++) ans = std::min(ans, f(i));
        return ans;
    }
};

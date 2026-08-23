// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

#include <vector>

class Solution {
public:
    std::vector<int> decode(std::vector<int>& encoded) {
        int n = encoded.size() + 1;
        int total = 0;
        for (int value = 1; value <= n; value++) {
            total ^= value;
        }
        int odd = 0;
        for (size_t i = 1; i < encoded.size(); i += 2) {
            odd ^= encoded[i];
        }
        std::vector<int> ans;
        ans.reserve(n);
        ans.push_back(total ^ odd);
        for (int value : encoded) {
            ans.push_back(ans.back() ^ value);
        }
        return ans;
    }
};

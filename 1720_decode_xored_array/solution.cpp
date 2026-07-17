// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

#include <vector>

class Solution {
public:
    std::vector<int> decode(std::vector<int>& encoded, int first) {
        std::vector<int> ans;
        ans.reserve(encoded.size() + 1);
        ans.push_back(first);
        for (int value : encoded) {
            ans.push_back(ans.back() ^ value);
        }
        return ans;
    }
};

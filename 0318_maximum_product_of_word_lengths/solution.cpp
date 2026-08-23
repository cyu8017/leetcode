// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxProduct(std::vector<std::string>& words) {
        std::vector<int> masks;
        std::vector<int> lengths;
        masks.reserve(words.size());
        lengths.reserve(words.size());

        for (const std::string& word : words) {
            int mask = 0;
            bool valid = true;
            for (char character : word) {
                int bit = 1 << (character - 'a');
                if (mask & bit) {
                    valid = false;
                    break;
                }
                mask |= bit;
            }
            masks.push_back(valid ? mask : 0);
            lengths.push_back(static_cast<int>(word.size()));
        }

        int best = 0;
        for (size_t left = 0; left < words.size(); left++) {
            if (masks[left] == 0) {
                continue;
            }
            for (size_t right = left + 1; right < words.size(); right++) {
                if (masks[right] == 0) {
                    continue;
                }
                if ((masks[left] & masks[right]) == 0) {
                    best = std::max(best, lengths[left] * lengths[right]);
                }
            }
        }

        return best;
    }
};

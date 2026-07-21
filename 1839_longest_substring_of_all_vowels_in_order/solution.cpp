// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

#include <string>
#include <vector>

class Solution {
public:
    int longestBeautifulSubstring(std::string word) {
        const std::string vowels = "aeiou";
        int best = 0;
        int n = static_cast<int>(word.size());
        for (int start = 0; start < n; ++start) {
            if (word[start] != 'a') {
                continue;
            }
            std::vector<int> counts(5, 0);
            for (int end = start; end < n; ++end) {
                char current = word[end];
                if (end > start && current < word[end - 1]) {
                    break;
                }
                size_t idx = vowels.find(current);
                if (idx == std::string::npos) {
                    break;
                }
                counts[idx] += 1;
                if (idx > 0 && counts[idx - 1] == 0) {
                    break;
                }
                bool allPresent = true;
                for (int count : counts) {
                    if (count == 0) {
                        allPresent = false;
                        break;
                    }
                }
                if (allPresent) {
                    best = std::max(best, end - start + 1);
                }
            }
        }
        return best;
    }
};

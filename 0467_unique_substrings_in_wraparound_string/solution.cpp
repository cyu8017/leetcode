// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int findSubstringInWraproundString(std::string s) {
        std::vector<int> counts(26, 0);
        int length = 0;
        for (int index = 0; index < static_cast<int>(s.size()); ++index) {
            if (index > 0 && (s[index] - s[index - 1] + 26) % 26 == 1) {
                ++length;
            } else {
                length = 1;
            }
            int position = s[index] - 'a';
            counts[position] = std::max(counts[position], length);
        }
        int total = 0;
        for (int count : counts) {
            total += count;
        }
        return total;
    }
};

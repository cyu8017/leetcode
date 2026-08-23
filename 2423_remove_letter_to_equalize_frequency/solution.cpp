// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

#include <string>
#include <unordered_map>

class Solution {
public:
    bool equalFrequency(std::string word) {
        for (int skip = 0; skip < (int)word.size(); skip++) {
            int cnt[26] = {};
            for (int i = 0; i < (int)word.size(); i++) {
                if (i == skip) continue;
                cnt[word[i] - 'a']++;
            }
            std::unordered_map<int, int> freq;
            for (int c : cnt) if (c > 0) freq[c]++;
            if ((int)freq.size() == 1) return true;
        }
        return false;
    }
};

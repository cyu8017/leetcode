// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool areOccurrencesEqual(std::string s) {
        std::vector<int> freq(26, 0);
        for (char c : s) freq[c - 'a']++;
        std::unordered_set<int> vals;
        for (int f : freq) if (f) vals.insert(f);
        return vals.size() == 1;
    }
};

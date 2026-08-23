// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

#include <string>
#include <vector>

class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        int n1 = static_cast<int>(s1.size());
        int n2 = static_cast<int>(s2.size());
        if (n1 > n2) {
            return false;
        }

        std::vector<int> need(26, 0);
        std::vector<int> window(26, 0);
        for (int i = 0; i < n1; ++i) {
            ++need[s1[i] - 'a'];
            ++window[s2[i] - 'a'];
        }

        int matches = 0;
        for (int i = 0; i < 26; ++i) {
            if (need[i] == window[i]) {
                ++matches;
            }
        }
        if (matches == 26) {
            return true;
        }

        for (int right = n1; right < n2; ++right) {
            int add = s2[right] - 'a';
            int remove = s2[right - n1] - 'a';

            if (window[add] == need[add]) {
                --matches;
            }
            ++window[add];
            if (window[add] == need[add]) {
                ++matches;
            }

            if (window[remove] == need[remove]) {
                --matches;
            }
            --window[remove];
            if (window[remove] == need[remove]) {
                ++matches;
            }

            if (matches == 26) {
                return true;
            }
        }
        return false;
    }
};

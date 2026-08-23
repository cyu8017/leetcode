// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

#include <string>
#include <vector>

class Solution {
public:
    int countPrefixSuffixPairs(std::vector<std::string>& words) {
        int ans = 0;
        for (int i = 0; i < (int)words.size(); i++) {
            const auto& s = words[i];
            for (int j = i + 1; j < (int)words.size(); j++) {
                const auto& t = words[j];
                if (t.size() >= s.size() && t.compare(0, s.size(), s) == 0 &&
                    t.compare(t.size() - s.size(), s.size(), s) == 0)
                    ans++;
            }
        }
        return ans;
    }
};

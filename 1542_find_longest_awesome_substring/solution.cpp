// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int longestAwesome(std::string s) {
        std::unordered_map<int, int> first;
        first[0] = -1;
        int mask = 0;
        int answer = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            mask ^= 1 << (s[i] - '0');
            auto it = first.find(mask);
            if (it != first.end()) {
                answer = std::max(answer, i - it->second);
            } else {
                first[mask] = i;
            }
            for (int bit = 0; bit < 10; ++bit) {
                int candidate = mask ^ (1 << bit);
                auto cit = first.find(candidate);
                if (cit != first.end()) {
                    answer = std::max(answer, i - cit->second);
                }
            }
        }
        return answer;
    }
};

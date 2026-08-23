// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int balancedString(std::string s) {
        std::unordered_map<char, int> count;
        for (char ch : s) {
            ++count[ch];
        }
        const int n = static_cast<int>(s.size());
        const int limit = n / 4;
        int left = 0, answer = n;
        for (int right = 0; right < n; ++right) {
            --count[s[right]];
            while (left < n && count['Q'] <= limit && count['W'] <= limit && count['E'] <= limit &&
                   count['R'] <= limit) {
                answer = std::min(answer, right - left + 1);
                ++count[s[left]];
                ++left;
            }
        }
        return answer;
    }
};

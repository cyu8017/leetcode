// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
    std::string s_;
    std::vector<std::vector<int>> memo_;

    int dp(int index, int remaining) {
        if (remaining < 0) {
            return 1000000000;
        }
        if (index == static_cast<int>(s_.size()) ||
            static_cast<int>(s_.size()) - index <= remaining) {
            return 0;
        }
        int& cached = memo_[index][remaining];
        if (cached != -1) {
            return cached;
        }
        int answer = dp(index + 1, remaining - 1);
        int same = 0;
        int removed = 0;
        for (int j = index; j < static_cast<int>(s_.size()); ++j) {
            if (s_[j] == s_[index]) {
                same += 1;
                int encoded = 1 + (same >= 2) + (same >= 10) + (same >= 100);
                answer = std::min(answer, encoded + dp(j + 1, remaining - removed));
            } else {
                removed += 1;
                if (removed > remaining) {
                    break;
                }
            }
        }
        return cached = answer;
    }

public:
    int getLengthOfOptimalCompression(std::string s, int k) {
        s_ = std::move(s);
        memo_.assign(s_.size() + 1, std::vector<int>(k + 1, -1));
        return dp(0, k);
    }
};

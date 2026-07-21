// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

#include <algorithm>
#include <string>

class Solution {
public:
    int minFlips(std::string s) {
        int n = static_cast<int>(s.size());
        std::string doubled = s + s;
        int alt0 = 0;
        int alt1 = 0;
        for (int i = 0; i < n; i++) {
            char expect0 = (i % 2 == 0) ? '0' : '1';
            char expect1 = (i % 2 == 0) ? '1' : '0';
            if (doubled[i] != expect0) alt0++;
            if (doubled[i] != expect1) alt1++;
        }
        int answer = std::min(alt0, alt1);
        for (int i = 0; i < n; i++) {
            char expect0 = (i % 2 == 0) ? '0' : '1';
            char expect1 = (i % 2 == 0) ? '1' : '0';
            if (doubled[i] != expect0) alt0--;
            if (doubled[i] != expect1) alt1--;

            char expect0Next = ((i + n) % 2 == 0) ? '0' : '1';
            char expect1Next = ((i + n) % 2 == 0) ? '1' : '0';
            if (doubled[i + n] != expect0Next) alt0++;
            if (doubled[i + n] != expect1Next) alt1++;

            answer = std::min({answer, alt0, alt1});
        }
        return answer;
    }
};

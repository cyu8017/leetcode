// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

#include <algorithm>
#include <string>

class Solution {
public:
    int minFlips(std::string s) {
        int ones = 0;
        for (char c : s) if (c == '1') ones++;
        int answer = ones;
        if (ones > 0) answer = ones - 1;
        int zeros = (int)s.size() - ones;
        answer = std::min(answer, zeros);
        if ((int)s.size() >= 2) {
            int cost = 0;
            for (int i = 0; i < (int)s.size(); i++) {
                char want = (i == 0 || i == (int)s.size() - 1) ? '1' : '0';
                if (s[i] != want) cost++;
            }
            answer = std::min(answer, cost);
        }
        return answer;
    }
};

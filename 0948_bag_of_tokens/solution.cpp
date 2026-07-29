// LeetCode 0948 - Bag of Tokens
// https://leetcode.com/problems/bag-of-tokens/

#include <algorithm>
#include <vector>

class Solution {
public:
    int bagOfTokensScore(std::vector<int>& tokens, int power) {
        std::sort(tokens.begin(), tokens.end());
        int i = 0, j = (int)tokens.size() - 1, score = 0, ans = 0;
        while (i <= j) {
            if (power >= tokens[i]) {
                power -= tokens[i++];
                score++;
                ans = std::max(ans, score);
            } else if (score) {
                power += tokens[j--];
                score--;
            } else break;
        }
        return ans;
    }
};

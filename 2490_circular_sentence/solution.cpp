// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

#include <string>

class Solution {
public:
    bool isCircularSentence(std::string sentence) {
        int n = (int)sentence.size();
        if (sentence[0] != sentence[n - 1]) return false;
        for (int i = 0; i < n; i++) {
            if (sentence[i] == ' ' && sentence[i - 1] != sentence[i + 1]) return false;
        }
        return true;
    }
};

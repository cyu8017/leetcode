// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    void reverseWords(vector<char>& s) {
        reverse(s.begin(), s.end());
        int start = 0;
        for (int end = 0; end <= static_cast<int>(s.size()); ++end) {
            if (end == static_cast<int>(s.size()) || s[end] == ' ') {
                reverse(s.begin() + start, s.begin() + end);
                start = end + 1;
            }
        }
    }
};
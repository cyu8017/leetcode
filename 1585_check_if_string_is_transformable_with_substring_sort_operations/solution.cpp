// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

#include <deque>
#include <string>
#include <vector>

class Solution {
public:
    bool isTransformable(std::string s, std::string t) {
        std::vector<std::deque<int>> positions(10);
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            positions[s[i] - '0'].push_back(i);
        }
        for (char ch : t) {
            const int d = ch - '0';
            if (positions[d].empty()) {
                return false;
            }
            const int index = positions[d].front();
            for (int smaller = 0; smaller < d; ++smaller) {
                if (!positions[smaller].empty() && positions[smaller].front() < index) {
                    return false;
                }
            }
            positions[d].pop_front();
        }
        return true;
    }
};

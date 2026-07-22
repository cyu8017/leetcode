// LeetCode 1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

#include <algorithm>
#include <string>

class Solution {
public:
    int minPartitions(std::string n) {
        return *std::max_element(n.begin(), n.end()) - '0';
    }
};

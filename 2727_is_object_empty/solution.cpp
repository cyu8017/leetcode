// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

#include <map>
#include <string>
#include <vector>

class Solution {
public:
    bool isEmpty(std::map<std::string, int>& obj) { return obj.empty(); }
    bool isEmpty(std::vector<int>& arr) { return arr.empty(); }
};

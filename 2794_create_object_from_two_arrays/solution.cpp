// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/
// JS-only problem; C++ string-map stand-in.

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::unordered_map<std::string, int> createObject(std::vector<std::string>& keysArr, std::vector<int>& valuesArr) {
        std::unordered_map<std::string, int> out;
        int n = std::min((int)keysArr.size(), (int)valuesArr.size());
        for (int i = 0; i < n; i++) {
            if (!out.count(keysArr[i])) out[keysArr[i]] = valuesArr[i];
        }
        return out;
    }
};

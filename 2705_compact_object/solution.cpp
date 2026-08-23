// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

#include <vector>
#include <map>
#include <string>

class Solution {
public:
    // JS compactObject stand-in for int vectors: drop zeros
    std::vector<int> compactObject(std::vector<int>& obj) {
        std::vector<int> out;
        for (int x : obj) if (x) out.push_back(x);
        return out;
    }
};

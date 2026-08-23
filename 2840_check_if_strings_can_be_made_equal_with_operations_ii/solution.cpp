// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

#include <array>
#include <string>

class Solution {
public:
    bool checkStrings(std::string s1, std::string s2) {
        std::array<int, 26> even1{}, odd1{}, even2{}, odd2{};
        for (int i = 0; i < (int)s1.size(); i++) {
            if (i % 2 == 0) { even1[s1[i] - 'a']++; even2[s2[i] - 'a']++; }
            else { odd1[s1[i] - 'a']++; odd2[s2[i] - 'a']++; }
        }
        return even1 == even2 && odd1 == odd2;
    }
};

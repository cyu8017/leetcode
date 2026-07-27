// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

#include <string>
#include <unordered_set>

class Solution {
public:
    int shortestWay(std::string source, std::string target) {
        std::unordered_set<char> sourceSet(source.begin(), source.end());
        for (char ch : target) {
            if (!sourceSet.count(ch)) {
                return -1;
            }
        }
        int ans = 0;
        int i = 0;
        int n = static_cast<int>(target.size());
        while (i < n) {
            ++ans;
            for (char ch : source) {
                if (i < n && target[i] == ch) {
                    ++i;
                }
            }
        }
        return ans;
    }
};

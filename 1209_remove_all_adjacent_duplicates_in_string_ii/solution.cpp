// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string removeDuplicates(std::string s, int k) {
        std::vector<std::pair<char, int>> stack;
        for (char ch : s) {
            if (!stack.empty() && stack.back().first == ch) {
                ++stack.back().second;
            } else {
                stack.push_back({ch, 1});
            }
            if (stack.back().second == k) {
                stack.pop_back();
            }
        }
        std::string answer;
        for (const auto& [ch, count] : stack) {
            answer.append(count, ch);
        }
        return answer;
    }
};

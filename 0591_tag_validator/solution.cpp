// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

#include <string>
#include <vector>

class Solution {
public:
    bool isValid(std::string code) {
        std::vector<std::string> stack;
        int i = 0;
        int n = static_cast<int>(code.size());

        while (i < n) {
            if (code.compare(i, 9, "<![CDATA[") == 0) {
                if (stack.empty()) {
                    return false;
                }
                size_t j = code.find("]]>", static_cast<size_t>(i) + 9);
                if (j == std::string::npos) {
                    return false;
                }
                i = static_cast<int>(j) + 3;
            } else if (code.compare(i, 2, "</") == 0) {
                size_t j = code.find('>', static_cast<size_t>(i) + 2);
                if (j == std::string::npos) {
                    return false;
                }
                std::string tag = code.substr(static_cast<size_t>(i) + 2, j - static_cast<size_t>(i) - 2);
                if (stack.empty() || stack.back() != tag) {
                    return false;
                }
                stack.pop_back();
                i = static_cast<int>(j) + 1;
                if (stack.empty() && i < n) {
                    return false;
                }
            } else if (code[i] == '<') {
                size_t j = code.find('>', static_cast<size_t>(i) + 1);
                if (j == std::string::npos) {
                    return false;
                }
                std::string tag = code.substr(static_cast<size_t>(i) + 1, j - static_cast<size_t>(i) - 1);
                if (tag.empty() || tag.size() > 9) {
                    return false;
                }
                for (char ch : tag) {
                    if (ch < 'A' || ch > 'Z') {
                        return false;
                    }
                }
                stack.push_back(tag);
                i = static_cast<int>(j) + 1;
            } else {
                if (stack.empty()) {
                    return false;
                }
                ++i;
            }
        }
        return stack.empty();
    }
};

// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

#include <string>
#include <vector>
#include <algorithm>

class TextEditor {
    std::vector<char> left, right;
    std::string suffix() {
        int start = std::max(0, (int)left.size() - 10);
        return std::string(left.begin() + start, left.end());
    }
public:
    TextEditor() {}

    void addText(std::string text) {
        left.insert(left.end(), text.begin(), text.end());
    }

    int deleteText(int k) {
        int deleted = 0;
        while (k > 0 && !left.empty()) { left.pop_back(); k--; deleted++; }
        return deleted;
    }

    std::string cursorLeft(int k) {
        while (k > 0 && !left.empty()) {
            right.push_back(left.back());
            left.pop_back();
            k--;
        }
        return suffix();
    }

    std::string cursorRight(int k) {
        while (k > 0 && !right.empty()) {
            left.push_back(right.back());
            right.pop_back();
            k--;
        }
        return suffix();
    }
};

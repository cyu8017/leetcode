// LeetCode 0385 - Mini Parser
// https://leetcode.com/problems/mini-parser/

#include <cctype>
#include <string>
#include <vector>

class NestedInteger {
public:
    NestedInteger() : isInteger_(false), integer_(0) {}
    explicit NestedInteger(int value) : isInteger_(true), integer_(value) {}

    bool isInteger() const {
        return isInteger_;
    }

    int getInteger() const {
        return integer_;
    }

    const std::vector<NestedInteger>& getList() const {
        return list_;
    }

    std::vector<NestedInteger>& getList() {
        return list_;
    }

private:
    bool isInteger_;
    int integer_;
    std::vector<NestedInteger> list_;
};

class Solution {
public:
    NestedInteger deserialize(std::string s) {
        if (s.empty() || s[0] != '[') {
            return NestedInteger(std::stoi(s));
        }

        std::vector<NestedInteger*> stack;
        NestedInteger* current = nullptr;
        int index = 0;
        bool negative = false;
        int number = 0;
        bool hasNumber = false;

        while (index < static_cast<int>(s.size())) {
            char ch = s[index];
            if (ch == '[') {
                auto* item = new NestedInteger();
                if (current) {
                    stack.push_back(current);
                }
                current = item;
            } else if (ch == '-') {
                negative = true;
            } else if (std::isdigit(ch)) {
                number = number * 10 + (ch - '0');
                hasNumber = true;
            } else if (ch == ',' || ch == ']') {
                if (hasNumber) {
                    current->getList().emplace_back(negative ? -number : number);
                    number = 0;
                    negative = false;
                    hasNumber = false;
                }
                if (ch == ']') {
                    if (stack.empty()) {
                        NestedInteger result = *current;
                        delete current;
                        return result;
                    }
                    NestedInteger* parent = stack.back();
                    stack.pop_back();
                    parent->getList().push_back(*current);
                    delete current;
                    current = parent;
                }
            }
            index += 1;
        }

        NestedInteger result = current ? *current : NestedInteger();
        delete current;
        return result;
    }
};

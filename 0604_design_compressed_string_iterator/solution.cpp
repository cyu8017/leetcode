// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

#include <string>
#include <vector>

class StringIterator {
    std::vector<char> chars_;
    std::vector<int> counts_;
    int index_ = 0;

public:
    StringIterator(std::string compressedString) {
        const int n = static_cast<int>(compressedString.size());
        int i = 0;
        while (i < n) {
            const char ch = compressedString[i++];
            int j = i;
            while (j < n && compressedString[j] >= '0' && compressedString[j] <= '9') {
                ++j;
            }
            chars_.push_back(ch);
            counts_.push_back(std::stoi(compressedString.substr(i, j - i)));
            i = j;
        }
    }

    char next() {
        if (!hasNext()) {
            return ' ';
        }
        const char ch = chars_[index_];
        --counts_[index_];
        if (counts_[index_] == 0) {
            ++index_;
        }
        return ch;
    }

    bool hasNext() { return index_ < static_cast<int>(chars_.size()); }
};

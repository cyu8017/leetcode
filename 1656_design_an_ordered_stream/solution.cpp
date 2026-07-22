// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

#include <string>
#include <vector>

class OrderedStream {
    std::vector<std::string> data_;
    int ptr_;

public:
    OrderedStream(int n) : data_(n + 1), ptr_(1) {}

    std::vector<std::string> insert(int idKey, std::string value) {
        data_[idKey] = value;
        std::vector<std::string> out;
        while (ptr_ < static_cast<int>(data_.size()) && !data_[ptr_].empty()) {
            out.push_back(data_[ptr_]);
            ++ptr_;
        }
        return out;
    }
};

// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

#include <vector>

class PeekingIterator {
    std::vector<int> values;
    int index = 0;
    int peeked = 0;
    bool hasPeeked = false;

public:
    PeekingIterator(const std::vector<int>& nums) : values(nums) {}

    int peek() {
        if (!hasPeeked) {
            peeked = values[index++];
            hasPeeked = true;
        }
        return peeked;
    }

    int next() {
        if (hasPeeked) {
            hasPeeked = false;
            return peeked;
        }
        return values[index++];
    }

    bool hasNext() {
        return hasPeeked || index < static_cast<int>(values.size());
    }
};

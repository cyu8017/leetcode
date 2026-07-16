// LeetCode 0379 - Design Phone Directory
// https://leetcode.com/problems/design-phone-directory/

#include <set>

class PhoneDirectory {
    std::set<int> available_;

public:
    PhoneDirectory(int maxNumbers) {
        for (int number = 0; number < maxNumbers; ++number) {
            available_.insert(number);
        }
    }

    int get() {
        if (available_.empty()) {
            return -1;
        }
        int number = *available_.begin();
        available_.erase(number);
        return number;
    }

    bool check(int number) {
        return available_.count(number) == 1;
    }

    void release(int number) {
        available_.insert(number);
    }
};

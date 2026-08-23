// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

#include <memory>

// JS Counter II stand-in
class CounterII {
    int init_, cur_;
public:
    CounterII(int init) : init_(init), cur_(init) {}
    int increment() { return ++cur_; }
    int decrement() { return --cur_; }
    int reset() { cur_ = init_; return cur_; }
};

class Solution {
public:
    CounterII* createCounter(int init) {
        return new CounterII(init);
    }
};

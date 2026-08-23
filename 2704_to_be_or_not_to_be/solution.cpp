// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

#include <stdexcept>

class Expect {
    int val;
public:
    Expect(int v) : val(v) {}
    bool toBe(int other) {
        if (val == other) return true;
        throw std::runtime_error("Not Equal");
    }
    bool notToBe(int other) {
        if (val != other) return true;
        throw std::runtime_error("Equal");
    }
};

class Solution {
public:
    Expect expect(int val) { return Expect(val); }
};

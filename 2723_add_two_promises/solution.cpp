// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

#include <functional>

class Solution {
public:
    // JS addTwoPromises stand-in
    int addTwoPromises(std::function<int()> promise1, std::function<int()> promise2) {
        return promise1() + promise2();
    }
};

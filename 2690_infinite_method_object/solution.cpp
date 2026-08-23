// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

#include <functional>
#include <string>

class Solution {
public:
    // JS infinite method object stand-in
    std::function<std::string(std::string)> createInfiniteObject() {
        return [](std::string) { return std::string("Hello World"); };
    }
};

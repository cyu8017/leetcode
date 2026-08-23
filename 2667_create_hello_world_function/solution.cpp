// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

#include <functional>
#include <string>

class Solution {
public:
    // JS hello world stand-in
    std::function<std::string()> createHelloWorld() {
        return []() { return std::string("Hello World"); };
    }
};

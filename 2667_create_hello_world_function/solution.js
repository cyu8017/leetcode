// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};

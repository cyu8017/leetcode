// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

import java.util.function.Supplier;

// JS hello world stand-in
class Solution {
    public Supplier<String> createHelloWorld() {
        return () -> "Hello World";
    }
}

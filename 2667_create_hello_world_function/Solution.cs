// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/

// JS hello world stand-in
using System;

public class Solution {
    public Func<string> CreateHelloWorld() {
        return () => "Hello World";
    }
}

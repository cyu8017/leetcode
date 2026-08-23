// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

// JS infinite method object stand-in
using System;

public class Solution {
    public Func<string, string> CreateInfiniteObject() {
        return _ => "Hello World";
    }
}

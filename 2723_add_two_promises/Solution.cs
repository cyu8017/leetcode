// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

// JS addTwoPromises stand-in
using System;

public class Solution {
    public int AddTwoPromises(Func<int> promise1, Func<int> promise2) {
        return promise1() + promise2();
    }
}

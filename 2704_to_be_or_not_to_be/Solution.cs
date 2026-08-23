// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

using System;

public class Expect {
    int val;
    public Expect(int v) { val = v; }
    public bool ToBe(int other) {
        if (val == other) return true;
        throw new Exception("Not Equal");
    }
    public bool NotToBe(int other) {
        if (val != other) return true;
        throw new Exception("Equal");
    }
}

public class Solution {
    public Expect Expect(int val) => new Expect(val);
}

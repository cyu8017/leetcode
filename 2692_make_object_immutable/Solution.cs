// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

// JS makeImmutable stand-in: return copy
using System.Collections.Generic;

public class Solution {
    public SortedDictionary<string, int> MakeImmutable(SortedDictionary<string, int> obj) {
        return new SortedDictionary<string, int>(obj);
    }
}

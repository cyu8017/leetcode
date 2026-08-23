// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

// JS array-of-objects-to-matrix stand-in
using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> JsonToMatrix(IList<SortedDictionary<string, string>> arr) {
        var keys = new SortedSet<string>();
        foreach (var obj in arr)
            foreach (var k in obj.Keys) keys.Add(k);
        var mat = new List<IList<string>>();
        mat.Add(new List<string>(keys));
        foreach (var obj in arr) {
            var row = new List<string>();
            foreach (var k in keys)
                row.Add(obj.TryGetValue(k, out var v) ? v : "");
            mat.Add(row);
        }
        return mat;
    }
}

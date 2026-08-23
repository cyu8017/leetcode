// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

using System.Collections.Generic;

public class Solution {
    public char KthCharacter(long k, int[] operations) {
        int shift = 0;
        var ops = new List<int>(operations);
        while (ops.Count > 0) {
            int op = ops[ops.Count - 1];
            ops.RemoveAt(ops.Count - 1);
            long half = 1L << ops.Count;
            if (k > half) {
                k -= half;
                if (op == 1) shift++;
            }
        }
        return (char)('a' + shift % 26);
    }
}

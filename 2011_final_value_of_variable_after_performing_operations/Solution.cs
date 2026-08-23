// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int x = 0;
        foreach (var op in operations) {
            if (op[1] == '+') x++;
            else x--;
        }
        return x;
    }
}

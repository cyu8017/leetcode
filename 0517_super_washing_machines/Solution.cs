// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

public class Solution {
    public int FindMinMoves(int[] machines) {
        int total = 0;
        foreach (int clothes in machines) {
            total += clothes;
        }
        int count = machines.Length;
        if (total % count != 0) {
            return -1;
        }
        int target = total / count;
        int prefix = 0;
        int result = 0;
        foreach (int clothes in machines) {
            int diff = clothes - target;
            prefix += diff;
            result = System.Math.Max(result, System.Math.Max(System.Math.Abs(prefix), diff));
        }
        return result;
    }
}

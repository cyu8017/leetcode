// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

class Solution {
    public int findMinMoves(int[] machines) {
        int total = 0;
        for (int clothes : machines) {
            total += clothes;
        }
        int count = machines.length;
        if (total % count != 0) {
            return -1;
        }
        int target = total / count;
        int prefix = 0;
        int result = 0;
        for (int clothes : machines) {
            int diff = clothes - target;
            prefix += diff;
            result = Math.max(result, Math.max(Math.abs(prefix), diff));
        }
        return result;
    }
}

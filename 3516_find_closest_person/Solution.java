// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

class Solution {
    public int findClosest(int x, int y, int z) {
        int a = Math.abs(x - z), b = Math.abs(y - z);
        if (a == b) return 0;
        return a < b ? 1 : 2;
    }
}

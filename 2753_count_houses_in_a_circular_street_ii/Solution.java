// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

class Solution {
    public int houseCount(int[] street, int k) {
        int n = street.length;
        if (n == 0) return 0;
        int start = -1;
        for (int i = 0; i < n; i++) {
            if (street[i] == 1) { start = i; break; }
        }
        if (start < 0) return 0;
        int count = 1, moves = 0, i2 = start;
        while (moves < k) {
            i2 = (i2 + 1) % n;
            moves++;
            if (i2 == start) break;
            if (street[i2] == 1) count++;
        }
        return count;
    }
}

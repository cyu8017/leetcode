// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

public class Solution {
    public int MinimumRefill(int[] plants, int capacityA, int capacityB) {
        int i = 0, j = plants.Length - 1;
        int a = capacityA, b = capacityB, ans = 0;
        while (i < j) {
            if (a < plants[i]) { ans++; a = capacityA; }
            a -= plants[i++];
            if (b < plants[j]) { ans++; b = capacityB; }
            b -= plants[j--];
        }
        if (i == j) {
            if (a >= b) { if (a < plants[i]) ans++; }
            else if (b < plants[i]) ans++;
        }
        return ans;
    }
}

// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

public class Solution {
    public int NumOfUnplacedFruits(int[] fruits, int[] baskets) {
        bool[] used = new bool[baskets.Length];
        int unplaced = 0;
        foreach (int f in fruits) {
            bool placed = false;
            for (int j = 0; j < baskets.Length; j++) {
                if (!used[j] && baskets[j] >= f) {
                    used[j] = true;
                    placed = true;
                    break;
                }
            }
            if (!placed) unplaced++;
        }
        return unplaced;
    }
}

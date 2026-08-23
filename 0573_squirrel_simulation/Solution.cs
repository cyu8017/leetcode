// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

public class Solution {
    public int MinDistance(int height, int width, int[] tree, int[] squirrel, int[][] nuts) {
        int total = 0;
        int bestSave = int.MinValue;
        foreach (int[] nut in nuts) {
            int treeDist = Dist(tree, nut);
            int squirrelDist = Dist(squirrel, nut);
            total += 2 * treeDist;
            int save = treeDist - squirrelDist;
            if (save > bestSave) bestSave = save;
        }
        return total - bestSave;
    }

    private int Dist(int[] a, int[] b) {
        return System.Math.Abs(a[0] - b[0]) + System.Math.Abs(a[1] - b[1]);
    }
}

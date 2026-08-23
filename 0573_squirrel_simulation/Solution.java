// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

class Solution {
    public int minDistance(int height, int width, int[] tree, int[] squirrel, int[][] nuts) {
        int total = 0;
        int bestSave = Integer.MIN_VALUE;
        for (int[] nut : nuts) {
            int treeDist = dist(tree, nut);
            int squirrelDist = dist(squirrel, nut);
            total += 2 * treeDist;
            int save = treeDist - squirrelDist;
            if (save > bestSave) {
                bestSave = save;
            }
        }
        return total - bestSave;
    }

    private int dist(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
}

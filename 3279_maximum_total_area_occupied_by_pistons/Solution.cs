// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

public class Solution {
    public long MaxArea(int height, int[] positions, string directions) {
        int n = positions.Length;
        int[] pos = (int[])positions.Clone();
        char[] dir = directions.ToCharArray();
        long best = 0;
        for (int t = 0; t <= 2 * height; t++) {
            long sum = 0;
            for (int i = 0; i < n; i++) sum += pos[i];
            if (sum > best) best = sum;
            for (int i = 0; i < n; i++) {
                if (dir[i] == 'U') {
                    if (pos[i] == height) { dir[i] = 'D'; pos[i]--; }
                    else pos[i]++;
                } else {
                    if (pos[i] == 0) { dir[i] = 'U'; pos[i]++; }
                    else pos[i]--;
                }
            }
        }
        return best;
    }
}

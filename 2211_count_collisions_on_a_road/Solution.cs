// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

public class Solution {
    public int CountCollisions(string directions) {
        int i = 0, j = directions.Length - 1;
        while (i < directions.Length && directions[i] == 'L') i++;
        while (j >= 0 && directions[j] == 'R') j--;
        int ans = 0;
        for (int k = i; k <= j; k++) if (directions[k] != 'S') ans++;
        return ans;
    }
}

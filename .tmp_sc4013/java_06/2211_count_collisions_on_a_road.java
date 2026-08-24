// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

class Solution {
    public int countCollisions(String directions) {
        int i = 0, j = directions.length() - 1;
        while (i < directions.length() && directions.charAt(i) == 'L') i++;
        while (j >= 0 && directions.charAt(j) == 'R') j--;
        int ans = 0;
        for (int k = i; k <= j; k++) if (directions.charAt(k) != 'S') ans++;
        return ans;
    }
}

// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        int n = words.length;
        int best = -1;
        for (int i = 0; i < n; i++) {
            if (words[i] == target) {
                int d = i - startIndex;
                if (d < 0) d = -d;
                if (n - d < d) d = n - d;
                if (best < 0 || d < best) best = d;
            }
        }
        return best;
    }
}

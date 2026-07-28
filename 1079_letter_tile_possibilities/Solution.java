// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

class Solution {
    public int numTilePossibilities(String tiles) {
        int[] count = new int[26];
        for (int i = 0; i < tiles.length(); i++) {
            count[tiles.charAt(i) - 'A']++;
        }
        return dfs(count);
    }

    private int dfs(int[] count) {
        int total = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] == 0) {
                continue;
            }
            count[i]--;
            total += 1 + dfs(count);
            count[i]++;
        }
        return total;
    }
}

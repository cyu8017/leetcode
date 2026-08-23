// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution {
    public boolean winnerOfGame(String colors) {
        int a = 0, b = 0;
        for (int i = 1; i + 1 < colors.length(); i++) {
            if (colors.charAt(i - 1) == colors.charAt(i) && colors.charAt(i) == colors.charAt(i + 1)) {
                if (colors.charAt(i) == 'A') a++;
                else b++;
            }
        }
        return a > b;
    }
}

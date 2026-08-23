// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

class Solution {
    public boolean canAliceWin(String[] a, String[] b) {
        int i = 0, j = 0;
        char last = 0;
        boolean alice = true;
        while (true) {
            if (alice) {
                while (i < a.length && a[i].charAt(0) <= last) i++;
                if (i == a.length) return false;
                last = a[i].charAt(a[i].length() - 1);
                i++;
            } else {
                while (j < b.length && b[j].charAt(0) <= last) j++;
                if (j == b.length) return true;
                last = b[j].charAt(b[j].length() - 1);
                j++;
            }
            alice = !alice;
        }
    }
}

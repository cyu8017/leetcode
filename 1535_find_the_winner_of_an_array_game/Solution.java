// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution {
    public int getWinner(int[] arr, int k) {
        int champion = arr[0];
        int wins = 0;
        for (int i = 1; i < arr.length; i++) {
            if (champion > arr[i]) {
                wins++;
            } else {
                champion = arr[i];
                wins = 1;
            }
            if (wins == k) {
                break;
            }
        }
        return champion;
    }
}

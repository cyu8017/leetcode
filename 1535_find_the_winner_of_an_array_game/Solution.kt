// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

class Solution {
    fun getWinner(arr: IntArray, k: Int): Int {
        var champion = arr[0]
        var wins = 0
        for (i in 1 until arr.size) {
            if (champion > arr[i]) {
                wins++
            } else {
                champion = arr[i]
                wins = 1
            }
            if (wins == k) break
        }
        return champion
    }
}

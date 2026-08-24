// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

interface Street {
    fun openDoor()
    fun closeDoor()
    fun isDoorOpen(): Boolean
    fun moveRight()
    fun moveLeft()
}

class Solution {
    fun countHouses(street: Street, k: Int): Int {
        for (i in 0 until k) {
            street.closeDoor()
            street.moveRight()
        }
        var ans = 0
        while (true) {
            ans++
            street.openDoor()
            street.moveRight()
            if (street.isDoorOpen()) break
        }
        return ans
    }
}

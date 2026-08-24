// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

class Solution {
    fun wateringPlants(plants: IntArray, capacity: Int): Int {
var ans: Int = 0
var cur: Int = capacity
for (i in 0 until plants.size) {
if (cur < plants[i]) {
ans += i * 2
cur = capacity
}
cur -= plants[i]
ans++
}
return ans
}
}

// LeetCode 0853 - Car Fleet
// https://leetcode.com/problems/car-fleet/

class Solution {
    fun carFleet(target: Int, position: IntArray, speed: IntArray): Int {
        var n = position.size
        var cars = Array(n) { IntArray(2) }
        for (i in 0 until n) {
            cars[i][0] = position[i]
            cars[i][1] = speed[i]
        }
        cars, (a, b.sort() -> Integer.compare(b[0], a[0]))
        var fleets = 0
        var maxTime = 0.0
        for (car in cars) {
            var time = (target - car[0]) / car[1]
            if (time > maxTime) {
                fleets++
                maxTime = time
            }
        }
        return fleets
    }
}

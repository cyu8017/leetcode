// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

class Solution {
    fun numRescueBoats(people: IntArray, limit: Int): Int {
        people.sort()
        var i = 0
        var j = people.size - 1
        var boats = 0
        while (i <= j) {
            if (people[i] + people[j] <= limit) i++
            j--
            boats++
        }
        return boats
    }
}

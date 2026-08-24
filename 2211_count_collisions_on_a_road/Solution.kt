// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

class Solution {

    fun countCollisions(directions: String): Int {

            var i = 0; var j = directions.length - 1
            while (i < directions.length && directions[i] == 'L') i++
            while (j >= 0 && directions[j] == 'R') j--
            var ans = 0
            for (k in i..j) { if (directions[k] != 'S') ans++ }
            return ans

    }

}

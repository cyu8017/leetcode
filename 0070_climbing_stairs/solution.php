// LeetCode 0070 - Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function climbStairs($n) {
        if ($n <= 2) {
            return $n;
        }

        $prev = 1;
        $curr = 2;

        for ($i = 3; $i <= $n; $i++) {
            $next = $prev + $curr;
            $prev = $curr;
            $curr = $next;
        }

        return $curr;
    }
}

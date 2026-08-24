<?php
// LeetCode 0276 - Paint Fence
// https://leetcode.com/problems/paint-fence/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numWays($n, $k) {
        if ($n === 0) {
            return 0;
        }
        if ($n === 1) {
            return $k;
        }
        if ($n === 2) {
            return $k * $k;
        }
        $prev2 = $k;
        $prev1 = $k * $k;
        for ($i = 3; $i <= $n; $i++) {
            $next = ($prev1 + $prev2) * ($k - 1);
            $prev2 = $prev1;
            $prev1 = $next;
        }
        return $prev1;
    }
}

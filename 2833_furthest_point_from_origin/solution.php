<?php
// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

class Solution {
    function furthestDistanceFromOrigin($moves) {
        $L = 0;
        $R = 0;
        $u = 0;
        $n = strlen($moves);
        for ($i = 0; $i < $n; $i++) {
            $c = $moves[$i];
            if ($c === 'L') $L++;
            else if ($c === 'R') $R++;
            else $u++;
        }
        return abs($L - $R) + $u;
    }
}

<?php
// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution {
    function maximizeExpressionOfThree($nums) {
        $inf = 1 << 30;
        $a = -$inf;
        $b = -$inf;
        $c = $inf;
        foreach ($nums as $x) {
            if ($x < $c) $c = $x;
            if ($x >= $a) { $b = $a; $a = $x; }
            else if ($x > $b) $b = $x;
        }
        return $a + $b - $c;
    }
}

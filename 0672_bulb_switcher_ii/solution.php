<?php
// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

class Solution {
    function flipLights($n, $presses) {
        $n = min($n, 3);
        if ($presses === 0) return 1;
        $onePress = [2, 3, 4];
        $twoPress = [2, 4, 7];
        $manyPress = [2, 4, 8];
        if ($presses === 1) return $onePress[$n - 1];
        if ($presses === 2) return $twoPress[$n - 1];
        return $manyPress[$n - 1];
    }
}

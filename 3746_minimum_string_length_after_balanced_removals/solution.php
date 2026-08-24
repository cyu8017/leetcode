<?php
// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution {
    function minLengthAfterRemovals($s) {
        $a = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === 'a') $a++;
        $b = $n - $a;
        return abs($a - $b);
    }
}

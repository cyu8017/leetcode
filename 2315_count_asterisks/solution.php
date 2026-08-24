<?php
// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

class Solution {
    function countAsterisks($s) {
        $ans = 0;
        $inside = false;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === '|') $inside = !$inside;
            elseif ($c === '*' && !$inside) $ans++;
        }
        return $ans;
    }
}

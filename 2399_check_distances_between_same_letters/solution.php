<?php
// LeetCode 2399 - Check Distances Between Same Letters
// https://leetcode.com/problems/check-distances-between-same-letters/

class Solution {
    function checkDistances($s, $distance) {
        $first = array_fill(0, 26, -1);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            if ($first[$c] === -1) $first[$c] = $i;
            elseif ($i - $first[$c] - 1 !== $distance[$c]) return false;
        }
        return true;
    }
}

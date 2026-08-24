<?php
// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

class Solution {
    function canReorderDoubled($arr) {
        $count = [];
        foreach ($arr as $x) $count[$x] = ($count[$x] ?? 0) + 1;
        $keys = array_keys($count);
        usort($keys, function ($a, $b) { return abs($a) <=> abs($b); });
        foreach ($keys as $x) {
            $need = $count[$x];
            if ($need === 0) continue;
            if (($count[2 * $x] ?? 0) < $need) return false;
            $count[2 * $x] -= $need;
        }
        return true;
    }
}

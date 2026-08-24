<?php
// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

class Solution {
    /**
     * @param Integer[] $hand
     * @param Integer $groupSize
     * @return Boolean
     */
    function isNStraightHand($hand, $groupSize) {
        if (count($hand) % $groupSize !== 0) return false;
        $count = [];
        foreach ($hand as $x) $count[$x] = ($count[$x] ?? 0) + 1;
        $keys = array_keys($count);
        sort($keys);
        foreach ($keys as $start) {
            $need = $count[$start] ?? 0;
            if ($need === 0) continue;
            for ($x = $start; $x < $start + $groupSize; $x++) {
                $c = $count[$x] ?? 0;
                if ($c < $need) return false;
                $count[$x] = $c - $need;
            }
        }
        return true;
    }
}

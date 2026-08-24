<?php
// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution {
    function minimumBoxes($apple, $capacity) {
        sort($capacity);
        $s = 0;
        foreach ($apple as $x) $s += $x;
        for ($i = 1; ; $i++) {
            $s -= $capacity[count($capacity) - $i];
            if ($s <= 0) return $i;
        }
    }
}

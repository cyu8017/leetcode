<?php
// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

class Solution {
    function assignElements($groups, $elements) {
        $maxV = 100001;
        $first = array_fill(0, $maxV, -1);
        for ($i = 0; $i < count($elements); $i++) {
            $e = $elements[$i];
            if ($e < $maxV && $first[$e] === -1) $first[$e] = $i;
        }
        $ans = array_fill(0, count($groups), -1);
        for ($gi = 0; $gi < count($groups); $gi++) {
            $g = $groups[$gi];
            $best = -1;
            for ($d = 1; $d * $d <= $g; $d++) {
                if ($g % $d === 0) {
                    if ($first[$d] !== -1 && ($best === -1 || $first[$d] < $best)) $best = $first[$d];
                    $other = intdiv($g, $d);
                    if ($first[$other] !== -1 && ($best === -1 || $first[$other] < $best)) $best = $first[$other];
                }
            }
            $ans[$gi] = $best;
        }
        return $ans;
    }
}

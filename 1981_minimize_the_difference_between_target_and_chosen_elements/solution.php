<?php
class Solution {
    /**
     * @param Integer[][] $mat
     * @param Integer $target
     * @return Integer
     */
    function minimizeTheDifference($mat, $target) {
        $possible = [0 => true];
        foreach ($mat as $row) {
            $uniq = array_unique($row);
            $nxt = [];
            foreach ($possible as $s => $_) {
                foreach ($uniq as $x) {
                    $nxt[$s + $x] = true;
                }
            }
            $kept = [];
            $minAbove = null;
            foreach ($nxt as $v => $_) {
                if ($v <= $target) {
                    $kept[$v] = true;
                } elseif ($minAbove === null || $v < $minAbove) {
                    $minAbove = $v;
                }
            }
            if ($minAbove !== null) {
                $kept[$minAbove] = true;
            }
            if (empty($kept)) {
                $possible = [min(array_keys($nxt)) => true];
            } else {
                $possible = $kept;
            }
        }
        $best = PHP_INT_MAX;
        foreach ($possible as $v => $_) {
            $best = min($best, abs($v - $target));
        }
        return $best;
    }
}

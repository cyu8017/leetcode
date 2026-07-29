<?php
// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

class Solution {
    /**
     * @param Integer[] $values
     * @param Integer[] $labels
     * @param Integer $numWanted
     * @param Integer $useLimit
     * @return Integer
     */
    function largestValsFromLabels($values, $labels, $numWanted, $useLimit) {
        $items = [];
        $n = count($values);
        for ($i = 0; $i < $n; $i++) {
            $items[] = [$values[$i], $labels[$i]];
        }
        usort($items, function ($a, $b) {
            return $b[0] <=> $a[0];
        });
        $used = [];
        $ans = 0;
        $taken = 0;
        foreach ($items as [$value, $label]) {
            if ($taken === $numWanted) {
                break;
            }
            if (($used[$label] ?? 0) < $useLimit) {
                $used[$label] = ($used[$label] ?? 0) + 1;
                $ans += $value;
                $taken++;
            }
        }
        return $ans;
    }
}

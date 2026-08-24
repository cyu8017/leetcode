<?php
// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution {
    private function minSteps($left, $right, $start) {
        if ($right <= $start) return $start - $left;
        if ($left >= $start) return $right - $start;
        return min(($start - $left) + ($right - $left), ($right - $start) + ($right - $left));
    }

    /**
     * @param Integer[][] $fruits
     * @param Integer $startPos
     * @param Integer $k
     * @return Integer
     */
    function maxTotalFruits($fruits, $startPos, $k) {
        $n = count($fruits);
        $pref = array_fill(0, $n + 1, 0);
        $pos = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $pos[$i] = $fruits[$i][0];
            $pref[$i + 1] = $pref[$i] + $fruits[$i][1];
        }
        $ans = 0;
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            while ($j < $n && $this->minSteps($pos[$i], $pos[$j], $startPos) > $k) $j++;
            if ($j <= $i) $ans = max($ans, $pref[$i + 1] - $pref[$j]);
        }
        $j = 0;
        for ($i = 0; $i < $n; $i++) {
            while ($j <= $i && $this->minSteps($pos[$j], $pos[$i], $startPos) > $k) $j++;
            $ans = max($ans, $pref[$i + 1] - $pref[$j]);
        }
        return $ans;
    }
}

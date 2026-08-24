<?php
// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

class Solution {
    function minSwaps($nums, $forbidden) {
        $n = count($nums);
        $freq = [];
        foreach ($nums as $x) {
            if (!isset($freq[$x])) $freq[$x] = 0;
            $freq[$x]++;
        }
        foreach ($forbidden as $x) {
            if (!isset($freq[$x])) $freq[$x] = 0;
            $freq[$x]++;
        }
        foreach ($freq as $c) {
            if ($c > $n) return -1;
        }
        $bad = [];
        $total = 0;
        $largest = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === $forbidden[$i]) {
                if (!isset($bad[$nums[$i]])) $bad[$nums[$i]] = 0;
                $bad[$nums[$i]]++;
                $total++;
                if ($bad[$nums[$i]] > $largest) $largest = $bad[$nums[$i]];
            }
        }
        if (intdiv($total + 1, 2) > $largest) return intdiv($total + 1, 2);
        return $largest;
    }
}

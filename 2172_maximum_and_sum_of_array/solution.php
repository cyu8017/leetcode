<?php
// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $numSlots
     * @return Integer
     */
    function maximumANDSum($nums, $numSlots) {
        $n = count($nums);
        $slots = $numSlots;
        $maxMask = 1;
        for ($i = 0; $i < $slots; $i++) $maxMask *= 3;
        $dp = array_fill(0, $maxMask, 0);
        for ($mask = 0; $mask < $maxMask; $mask++) {
            $cnt = 0;
            $x = $mask;
            while ($x > 0) { $cnt += $x % 3; $x = intdiv($x, 3); }
            if ($cnt >= $n) continue;
            $v = $nums[$cnt];
            $bas = 1;
            for ($s = 1; $s <= $slots; $s++) {
                $occ = intdiv($mask, $bas) % 3;
                if ($occ < 2) {
                    $nm = $mask + $bas;
                    $dp[$nm] = max($dp[$nm], $dp[$mask] + ($v & $s));
                }
                $bas *= 3;
            }
        }
        $best = 0;
        foreach ($dp as $v) $best = max($best, $v);
        return $best;
    }
}

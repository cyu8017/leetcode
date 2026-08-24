<?php
// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

class Solution {
    function maximumTotalValue($value, $decay, $m) {
        $mod = 1000000007;
        if ($this->countAtLeast($value, $decay, 1) <= $m) {
            $sum = 0;
            for ($i = 0; $i < count($value); $i++) {
                $terms = intdiv($value[$i] - 1, $decay[$i]) + 1;
                $sum = ($sum + $terms * $value[$i] - $decay[$i] * $terms * ($terms - 1) / 2) % $mod;
            }
            return $sum;
        }
        $high = 0;
        foreach ($value as $v) if ($v > $high) $high = $v;
        $low = 1;
        while ($low < $high) {
            $mid = intdiv($low + $high + 1, 2);
            if ($this->countAtLeast($value, $decay, $mid) >= $m) $low = $mid;
            else $high = $mid - 1;
        }
        $threshold = $low;
        $count = 0;
        $sum = 0;
        for ($i = 0; $i < count($value); $i++) {
            if ($value[$i] < $threshold) continue;
            $terms = intdiv($value[$i] - $threshold, $decay[$i]) + 1;
            $count += $terms;
            $sum = ($sum + ($terms * $value[$i] - $decay[$i] * $terms * ($terms - 1) / 2) % $mod) % $mod;
        }
        $sum = ($sum - (($count - $m) % $mod) * ($threshold % $mod)) % $mod;
        if ($sum < 0) $sum += $mod;
        return $sum;
    }

    private function countAtLeast($value, $decay, $threshold) {
        $count = 0;
        for ($i = 0; $i < count($value); $i++) {
            if ($value[$i] >= $threshold) $count += intdiv($value[$i] - $threshold, $decay[$i]) + 1;
        }
        return $count;
    }
}

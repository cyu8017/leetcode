<?php
// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

class Solution {
    function countValidSubarrays($nums, $x) {
        $byRemainder = array_fill(0, 10, []);
        $byRemainder[0][] = 0;
        $prefix = 0;
        $answer = 0;
        foreach ($nums as $value) {
            $prefix += $value;
            $required = (($prefix - $x) % 10 + 10) % 10;
            $values = $byRemainder[$required];
            for ($power = 1; $x * $power <= $prefix; $power *= 10) {
                $low = $x * $power;
                $high = ($x + 1) * $power - 1;
                $minPrefix = $prefix - $high;
                $maxPrefix = $prefix - $low;
                $left = $this->lowerBound($values, $minPrefix);
                $right = $this->upperBound($values, $maxPrefix);
                $answer += $right - $left;
                if ($power > intdiv($prefix, 10)) break;
            }
            $byRemainder[$prefix % 10][] = $prefix;
        }
        return $answer;
    }

    private function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function upperBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}

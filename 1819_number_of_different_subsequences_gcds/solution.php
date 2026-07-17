<?php
// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countDifferentSubsequenceGCDs($nums) {
        $maxVal = max($nums);
        $present = array_fill(0, $maxVal + 1, false);
        foreach ($nums as $num) {
            $present[$num] = true;
        }

        $ans = 0;
        for ($g = 1; $g <= $maxVal; $g++) {
            $has = false;
            $gcdVal = 0;
            for ($multiple = $g; $multiple <= $maxVal; $multiple += $g) {
                if ($present[$multiple]) {
                    $has = true;
                    $gcdVal = $this->gcd($gcdVal, intdiv($multiple, $g));
                    if ($gcdVal === 1) {
                        break;
                    }
                }
            }
            if ($has && $gcdVal === 1) {
                $ans++;
            }
        }
        return $ans;
    }

    /**
     * @param int $a
     * @param int $b
     * @return int
     */
    private function gcd($a, $b) {
        while ($b !== 0) {
            $temp = $a % $b;
            $a = $b;
            $b = $temp;
        }
        return $a;
    }
}

<?php
// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

class Solution {
    function minOperations($nums, $target) {
        $cnt = array_fill(0, 32, 0);
        $sum = 0;
        foreach ($nums as $v) {
            $sum += $v;
            $b = 0;
            while ((1 << $b) < $v) $b++;
            $cnt[$b]++;
        }
        if ($sum < $target) return -1;
        $ans = 0;
        for ($i = 0; $i < 31; $i++) {
            if (($target & (1 << $i)) !== 0) {
                if ($cnt[$i] > 0) $cnt[$i]--;
                else {
                    $j = $i + 1;
                    while ($j < 32 && $cnt[$j] === 0) $j++;
                    if ($j === 32) return -1;
                    while ($j > $i) {
                        $cnt[$j]--;
                        $cnt[$j - 1] += 2;
                        $ans++;
                        $j--;
                    }
                    $cnt[$i]--;
                }
            }
            $cnt[$i + 1] += intdiv($cnt[$i], 2);
        }
        return $ans;
    }
}

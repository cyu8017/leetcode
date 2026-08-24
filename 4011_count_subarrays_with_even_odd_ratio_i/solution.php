<?php
// LeetCode 4011 - Count Subarrays With Even Odd Ratio I
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

class Solution {
    function countRatioSubarrays($nums, $a, $b) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $y = 0;
            for ($j = $i; $j < $n; $j++) {
                $y += $nums[$j] % 2;
                $x = $j - $i + 1 - $y;
                if ($y > 0 && $x * $b <= $y * $a) $ans++;
            }
        }
        return $ans;
    }
}

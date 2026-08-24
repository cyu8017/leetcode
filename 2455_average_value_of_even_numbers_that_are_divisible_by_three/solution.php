<?php
// LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
// https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution {
    function averageValue($nums) {
        $sum = 0;
        $cnt = 0;
        foreach ($nums as $x) {
            if ($x % 6 === 0) {
                $sum += $x;
                $cnt++;
            }
        }
        return $cnt === 0 ? 0 : intdiv($sum, $cnt);
    }
}

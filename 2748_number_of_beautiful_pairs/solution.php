<?php
// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
    function countBeautifulPairs($nums) {
        $gcd = function($a, $b) {
            while ($b) { $t = $a % $b; $a = $b; $b = $t; }
            return $a;
        };
        $firstDigit = function($x) {
            while ($x >= 10) $x = intdiv($x, 10);
            return $x;
        };
        $ans = 0;
        $freq = array_fill(0, 10, 0);
        foreach ($nums as $x) {
            $last = $x % 10;
            for ($d = 1; $d <= 9; $d++)
                if ($freq[$d] > 0 && $gcd($d, $last) === 1) $ans += $freq[$d];
            $freq[$firstDigit($x)]++;
        }
        return $ans;
    }
}

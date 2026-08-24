<?php
// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution {
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $nxt = array_fill(0, $n + 1, 0);
        $nxt[$n] = $n;
        for ($i = $n - 1; $i >= 0; $i--) {
            $nxt[$i] = $nxt[$i + 1];
            if ($s[$i] === '0') $nxt[$i] = $i;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt0 = $s[$i] === '0' ? 1 : 0;
            $j = $i;
            while ($j < $n && $cnt0 * $cnt0 <= $n) {
                $cnt1 = $nxt[$j + 1] - $i - $cnt0;
                if ($cnt1 >= $cnt0 * $cnt0) {
                    $ans += min($nxt[$j + 1] - $j, $cnt1 - $cnt0 * $cnt0 + 1);
                }
                $j = $nxt[$j + 1];
                $cnt0++;
            }
        }
        return $ans;
    }
}

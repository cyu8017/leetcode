<?php
// LeetCode 2845 - Count of Interesting Subarrays
// https://leetcode.com/problems/count-of-interesting-subarrays/

class Solution {
    function countInterestingSubarrays($nums, $modulo, $k) {
        $freq = [0 => 1];
        $ans = 0;
        $pref = 0;
        foreach ($nums as $v) {
            if ($v % $modulo === $k) $pref++;
            $need = ($pref - $k) % $modulo;
            if ($need < 0) $need += $modulo;
            $ans += $freq[$need] ?? 0;
            $key = $pref % $modulo;
            if (!isset($freq[$key])) $freq[$key] = 0;
            $freq[$key]++;
        }
        return $ans;
    }
}

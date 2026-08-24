<?php
// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minimalKSum($nums, $k) {
        sort($nums);
        $ans = 0;
        $prev = 0;
        foreach ($nums as $x) {
            if ($x <= $prev) continue;
            $start = $prev + 1;
            $end = $x - 1;
            if ($start <= $end) {
                $cnt = $end - $start + 1;
                if ($cnt > $k) { $end = $start + $k - 1; $cnt = $k; }
                $ans += intdiv(($start + $end) * $cnt, 2);
                $k -= $cnt;
                if ($k === 0) return $ans;
            }
            $prev = $x;
        }
        $s = $prev + 1;
        $e = $s + $k - 1;
        $ans += intdiv(($s + $e) * $k, 2);
        return $ans;
    }
}

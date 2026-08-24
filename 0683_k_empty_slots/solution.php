<?php
// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

class Solution {
    function kEmptySlots($bulbs, $k) {
        $n = count($bulbs);
        $days = array_fill(0, $n, 0);
        for ($day = 1; $day <= $n; $day++) $days[$bulbs[$day - 1] - 1] = $day;
        $ans = PHP_INT_MAX;
        $i = 0;
        while ($i < $n - $k - 1) {
            $left = $i;
            $right = $i + $k + 1;
            $j = $left + 1;
            while ($j < $right && $days[$j] > $days[$left] && $days[$j] > $days[$right]) $j++;
            if ($j === $right) {
                $ans = min($ans, max($days[$left], $days[$right]));
                $i++;
            } else $i = $j;
        }
        return $ans === PHP_INT_MAX ? -1 : $ans;
    }
}

<?php
// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

class Solution {
    function countOfPairs($n, $x, $y) {
        if ($x > $y) { $t = $x; $x = $y; $y = $t; }
        $A = array_fill(0, $n, 0);
        for ($i = 1; $i <= $n; $i++) {
            $A[0] += 2;
            $A[min($i - 1, abs($i - $y) + $x)] -= 1;
            $A[min($n - $i, abs($i - $x) + 1 + ($n - $y))] -= 1;
            $A[min(abs($i - $x), abs($y - $i) + 1)] += 1;
            $A[min(abs($i - $x) + 1, abs($y - $i))] += 1;
            $r = max($x - $i, 0) + max($i - $y, 0);
            $A[$r + intdiv($y - $x, 2)] -= 1;
            $A[$r + intdiv($y - $x + 1, 2)] -= 1;
        }
        for ($i = 1; $i < $n; $i++) $A[$i] += $A[$i - 1];
        return $A;
    }
}

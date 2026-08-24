<?php
// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution {
    function countOfPairs($n, $x, $y) {
        $ans = array_fill(0, $n, 0);
        $x--;
        $y--;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $a = $j - $i;
                $b = abs($x - $i) + abs($y - $j) + 1;
                $c = abs($x - $j) + abs($y - $i) + 1;
                $ans[min($a, min($b, $c)) - 1] += 2;
            }
        }
        return $ans;
    }
}

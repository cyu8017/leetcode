<?php
// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

class Solution {
    function maximumBooks($books) {
        $n = count($books);
        $dp = array_fill(0, $n, 0);
        $stack = [];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            while (count($stack) > 0 && $books[$stack[count($stack) - 1]] >= $books[$i] - ($i - $stack[count($stack) - 1])) {
                array_pop($stack);
            }
            if (count($stack) === 0) {
                $dp[$i] = $this->rangeSum(0, $i, $books[$i]);
            } else {
                $j = $stack[count($stack) - 1];
                $dp[$i] = $dp[$j] + $this->rangeSum($j + 1, $i, $books[$i]);
            }
            $ans = max($ans, $dp[$i]);
            $stack[] = $i;
        }
        return $ans;
    }

    private function rangeSum($l, $r, $h) {
        $width = $r - $l + 1;
        if ($h >= $width) return intdiv($width * (2 * $h - $width + 1), 2);
        return intdiv($h * ($h + 1), 2);
    }
}

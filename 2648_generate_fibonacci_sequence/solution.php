<?php
// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

class Solution {
    function fibGenerator() {
        $a = 0;
        $b = 1;
        while (true) {
            yield $a;
            $tmp = $a + $b;
            $a = $b;
            $b = $tmp;
        }
    }
}

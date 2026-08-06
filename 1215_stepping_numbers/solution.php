<?php
// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

class Solution {
    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function countSteppingNumbers($low, $high) {
        $answer = $low === 0 ? [0] : [];
        $queue = range(1, 9);
        $head = 0;
        while ($head < count($queue)) {
            $x = $queue[$head++];
            if ($x > $high) continue;
            if ($x >= $low) $answer[] = $x;
            $last = $x % 10;
            if ($last > 0) $queue[] = $x * 10 + $last - 1;
            if ($last < 9) $queue[] = $x * 10 + $last + 1;
        }
        sort($answer);
        return $answer;
    }
}

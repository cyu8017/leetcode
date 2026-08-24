<?php
// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

class Solution {
    function partitionLabels($s) {
        $last = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $last[ord($s[$i]) - 97] = $i;
        $start = 0;
        $end = 0;
        $answer = [];
        for ($i = 0; $i < $n; $i++) {
            $end = max($end, $last[ord($s[$i]) - 97]);
            if ($i === $end) {
                $answer[] = $end - $start + 1;
                $start = $i + 1;
            }
        }
        return $answer;
    }
}

<?php
// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution {
    function minimumPartition($s, $k) {
        $ans = 1;
        $cur = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $d = ord($s[$i]) - 48;
            if ($d > $k) return -1;
            $nxt = $cur * 10 + $d;
            if ($nxt > $k) {
                $ans++;
                $cur = $d;
            } else {
                $cur = $nxt;
            }
        }
        return $ans;
    }
}

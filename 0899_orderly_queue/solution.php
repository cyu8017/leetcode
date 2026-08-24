<?php
// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

class Solution {
    function orderlyQueue($s, $k) {
        if ($k > 1) {
            $chars = str_split($s);
            sort($chars);
            return implode("", $chars);
        }
        $best = $s;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            $cand = substr($s, $i) . substr($s, 0, $i);
            if ($cand < $best) $best = $cand;
        }
        return $best;
    }
}

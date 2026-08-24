<?php
// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

class Solution {
    function countWays($word1, $word2, $target) {
        $mod = 1000000007;
        $n1 = strlen($word1);
        $n2 = strlen($word2);
        $size = ($n1 + 1) * ($n2 + 1) * 4;
        $dp = array_fill(0, $size, 0);
        $next = array_fill(0, $size, 0);
        $dp[$this->idx(0, 0, 0, $n2)] = 1;
        $tlen = strlen($target);
        for ($ti = 0; $ti < $tlen; $ti++) {
            $ch = $target[$ti];
            $next = array_fill(0, $size, 0);
            for ($j = 0; $j <= $n2; $j++) {
                $prefix = array_fill(0, 4, 0);
                for ($a = 0; $a < $n1; $a++) {
                    for ($mask = 0; $mask < 4; $mask++) {
                        $prefix[$mask] += $dp[$this->idx($a, $j, $mask, $n2)];
                        if ($prefix[$mask] >= $mod) $prefix[$mask] -= $mod;
                    }
                    if ($word1[$a] == $ch) {
                        for ($mask = 0; $mask < 4; $mask++) {
                            $at = $this->idx($a + 1, $j, $mask | 1, $n2);
                            $next[$at] += $prefix[$mask];
                            if ($next[$at] >= $mod) $next[$at] -= $mod;
                        }
                    }
                }
            }
            for ($i = 0; $i <= $n1; $i++) {
                $prefix = array_fill(0, 4, 0);
                for ($b = 0; $b < $n2; $b++) {
                    for ($mask = 0; $mask < 4; $mask++) {
                        $prefix[$mask] += $dp[$this->idx($i, $b, $mask, $n2)];
                        if ($prefix[$mask] >= $mod) $prefix[$mask] -= $mod;
                    }
                    if ($word2[$b] == $ch) {
                        for ($mask = 0; $mask < 4; $mask++) {
                            $at = $this->idx($i, $b + 1, $mask | 2, $n2);
                            $next[$at] += $prefix[$mask];
                            if ($next[$at] >= $mod) $next[$at] -= $mod;
                        }
                    }
                }
            }
            $tmp = $dp;
            $dp = $next;
            $next = $tmp;
        }
        $answer = 0;
        for ($i = 0; $i <= $n1; $i++) {
            for ($j = 0; $j <= $n2; $j++) {
                $answer += $dp[$this->idx($i, $j, 3, $n2)];
                if ($answer >= $mod) $answer -= $mod;
            }
        }
        return $answer;
    }

    private function idx($i, $j, $mask, $n2) {
        return (($i * ($n2 + 1) + $j) * 4) + $mask;
    }
}

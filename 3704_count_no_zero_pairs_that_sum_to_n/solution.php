<?php
// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

class Solution {
    function countNoZeroPairs($n) {
        $s = (string)$n;
        $m = strlen($s);
        $digits = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; $i++) $digits[$i] = ord($s[$m - 1 - $i]) - 48;
        $dp = [];
        for ($c = 0; $c < 2; $c++)
            for ($a = 0; $a < 2; $a++)
                $dp[$c][$a] = [0, 0];
        $dp[0][1][1] = 1;
        for ($pos = 0; $pos < $m + 1; $pos++) {
            $ndp = [];
            for ($c = 0; $c < 2; $c++)
                for ($a = 0; $a < 2; $a++)
                    $ndp[$c][$a] = [0, 0];
            $target = $digits[$pos];
            for ($carry = 0; $carry <= 1; $carry++) {
                for ($aliveA = 0; $aliveA <= 1; $aliveA++) {
                    for ($aliveB = 0; $aliveB <= 1; $aliveB++) {
                        $ways = $dp[$carry][$aliveA][$aliveB];
                        if ($ways === 0) continue;
                        $A = [];
                        if ($aliveA === 1) {
                            for ($d = 1; $d <= 9; $d++) $A[] = [$d, 1];
                            if ($pos > 0) $A[] = [0, 0];
                        } else {
                            $A[] = [0, 0];
                        }
                        $B = [];
                        if ($aliveB === 1) {
                            for ($d = 1; $d <= 9; $d++) $B[] = [$d, 1];
                            if ($pos > 0) $B[] = [0, 0];
                        } else {
                            $B[] = [0, 0];
                        }
                        foreach ($A as $pa) {
                            $da = $pa[0];
                            $na = $pa[1];
                            foreach ($B as $pb) {
                                $db = $pb[0];
                                $nb = $pb[1];
                                $sum = $da + $db + $carry;
                                if ($sum % 10 !== $target) continue;
                                $ncarry = intdiv($sum, 10);
                                $ndp[$ncarry][$na][$nb] += $ways;
                            }
                        }
                    }
                }
            }
            $dp = $ndp;
        }
        return $dp[0][0][0];
    }
}

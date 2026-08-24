<?php
// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/

class Solution {
    function minOperations($nums, $k) {
        $evenFreq = array_fill(0, $k, 0);
        $oddFreq = array_fill(0, $k, 0);
        for ($i = 0; $i < count($nums); $i++) {
            if ($i % 2 == 0) $evenFreq[$nums[$i] % $k]++;
            else $oddFreq[$nums[$i] % $k]++;
        }
        $evenCost = $this->costs($evenFreq, $k);
        $oddCost = $this->costs($oddFreq, $k);
        $best1 = 1 << 62;
        $best2 = 1 << 62;
        $bestIndex = -1;
        for ($i = 0; $i < $k; $i++) {
            $x = $oddCost[$i];
            if ($x < $best1) {
                $best2 = $best1;
                $best1 = $x;
                $bestIndex = $i;
            } else if ($x < $best2) $best2 = $x;
        }
        $ans = 1 << 62;
        for ($x = 0; $x < $k; $x++) {
            $other = ($x == $bestIndex) ? $best2 : $best1;
            $ans = min($ans, $evenCost[$x] + $other);
        }
        return $ans;
    }

    private function costs($freq, $k) {
        $dbl = array_fill(0, 2 * $k, 0);
        for ($i = 0; $i < 2 * $k; $i++) $dbl[$i] = $freq[$i % $k];
        $countPrefix = array_fill(0, 2 * $k + 1, 0);
        $weightedPrefix = array_fill(0, 2 * $k + 1, 0);
        for ($i = 0; $i < 2 * $k; $i++) {
            $countPrefix[$i + 1] = $countPrefix[$i] + $dbl[$i];
            $weightedPrefix[$i + 1] = $weightedPrefix[$i] + $i * $dbl[$i];
        }
        $res = array_fill(0, $k, 0);
        $cw = intdiv($k, 2);
        $cc = intdiv($k - 1, 2);
        for ($t = 0; $t < $k; $t++) {
            $cnt = $countPrefix[$t + $cw + 1] - $countPrefix[$t];
            $sum = $weightedPrefix[$t + $cw + 1] - $weightedPrefix[$t];
            $res[$t] += $sum - $t * $cnt;
            if ($cc > 0) {
                $cnt2 = $countPrefix[$t + $k] - $countPrefix[$t + $k - $cc];
                $sum2 = $weightedPrefix[$t + $k] - $weightedPrefix[$t + $k - $cc];
                $res[$t] += ($t + $k) * $cnt2 - $sum2;
            }
        }
        return $res;
    }
}

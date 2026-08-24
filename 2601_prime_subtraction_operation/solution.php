<?php
// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

class Solution {
    function primeSubOperation($nums) {
        $maxV = 0;
        foreach ($nums as $x) if ($x > $maxV) $maxV = $x;
        $isP = array_fill(0, $maxV + 1, true);
        if ($maxV >= 0) $isP[0] = false;
        if ($maxV >= 1) $isP[1] = false;
        for ($i = 2; $i * $i <= $maxV; $i++) {
            if (!$isP[$i]) continue;
            for ($j = $i * $i; $j <= $maxV; $j += $i) $isP[$j] = false;
        }
        $primes = [];
        for ($i = 2; $i <= $maxV; $i++) if ($isP[$i]) $primes[] = $i;
        $prev = 0;
        foreach ($nums as $x) {
            $need = $x - $prev;
            $best = -1;
            foreach ($primes as $p) {
                if ($p >= $need) break;
                $best = $p;
            }
            $cur = $best < 0 ? $x : $x - $best;
            if ($cur <= $prev) return false;
            $prev = $cur;
        }
        return true;
    }
}

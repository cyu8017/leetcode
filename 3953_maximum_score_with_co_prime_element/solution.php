<?php
// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

class Solution {
    function maxScore($nums, $maxVal) {
        $limit = $maxVal;
        $frequency = array_fill(0, 100001, 0);
        foreach ($nums as $x) {
            $frequency[$x]++;
            if ($x > $limit) $limit = $x;
        }
        $divisible = array_fill(0, $limit + 1, 0);
        for ($d = 1; $d <= $limit; $d++) {
            for ($multiple = $d; $multiple <= $limit; $multiple += $d) {
                if ($multiple < count($frequency)) $divisible[$d] += $frequency[$multiple];
            }
        }
        $best = -count($nums);
        $checked = array_fill(0, $limit + 1, false);
        for ($x = 1; $x <= $maxVal; $x++) {
            $best = max($best, $this->evaluate($x, $x < count($frequency) && $frequency[$x] > 0, $checked, $divisible));
        }
        foreach ($nums as $x) {
            $best = max($best, $this->evaluate($x, true, $checked, $divisible));
        }
        return $best;
    }

    private function evaluate($x, $exists, &$checked, $divisible) {
        if ($checked[$x]) return intdiv(-2147483648, 4);
        $checked[$x] = true;
        $bad = $this->badCount($x, $divisible);
        if ($exists) $cost = $x > 1 ? $bad - 1 : 0;
        else $cost = $bad > 0 ? $bad : 1;
        return $x - $cost;
    }

    private function badCount($x, $divisible) {
        $primes = [];
        $y = $x;
        for ($p = 2; $p * $p <= $y; $p++) {
            if ($y % $p === 0) {
                $primes[] = $p;
                while ($y % $p === 0) $y = intdiv($y, $p);
            }
        }
        if ($y > 1) $primes[] = $y;
        $bad = 0;
        $psz = count($primes);
        for ($mask = 1; $mask < (1 << $psz); $mask++) {
            $product = 1;
            $bits = 0;
            for ($i = 0; $i < $psz; $i++) {
                if ((($mask >> $i) & 1) !== 0) {
                    $product *= $primes[$i];
                    $bits++;
                }
            }
            if ($bits % 2 === 1) $bad += $divisible[$product];
            else $bad -= $divisible[$product];
        }
        return $bad;
    }
}

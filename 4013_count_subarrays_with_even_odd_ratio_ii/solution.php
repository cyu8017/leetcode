<?php
// LeetCode 4013 - Count Subarrays With Even Odd Ratio II
// https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

class Solution {
    function countRatioSubarrays($nums, $a, $b) {
        $n = count($nums);
        $s = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % 2 === 1) $s[$i + 1] = $s[$i] + $a;
            else $s[$i + 1] = $s[$i] - $b;
        }
        $st = $s;
        sort($st);
        $uniq = [];
        foreach ($st as $v) {
            if (empty($uniq) || $v !== $uniq[count($uniq) - 1]) $uniq[] = $v;
        }
        $st = $uniq;
        $bit = array_fill(0, count($st) + 2, 0);
        $ans = 0;
        foreach ($s as $v) {
            $x = $this->lowerBound($st, $v) + 1;
            $ans += $this->query($bit, $x);
            $this->update($bit, $x, 1);
        }
        return $ans;
    }

    private function update(&$c, $x, $delta) {
        $n = count($c) - 1;
        for (; $x <= $n; $x += $x & -$x) $c[$x] += $delta;
    }

    private function query($c, $x) {
        $sum = 0;
        for (; $x > 0; $x -= $x & -$x) $sum += $c[$x];
        return $sum;
    }

    private function lowerBound($a, $x) {
        $lo = 0;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($a[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}

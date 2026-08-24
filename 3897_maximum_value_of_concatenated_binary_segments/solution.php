<?php
// LeetCode 3897 - Maximum Value of Concatenated Binary Segments
// https://leetcode.com/problems/maximum-value-of-concatenated-binary-segments/

class Solution {
    const MOD = 1000000007;
    function group($p) {
        if ($p[1] === 0) return 0;
        if ($p[0] > 0) return 1;
        return 2;
    }
    function maxValue($nums1, $nums0) {
        $n = count($nums1);
        $pairs = [];
        for ($i = 0; $i < $n; $i++) $pairs[] = [$nums1[$i], $nums0[$i]];
        $b = 0;
        for ($i = 0; $i < $n; $i++) $b += $nums1[$i] + $nums0[$i];
        usort($pairs, function($a, $c) {
            $g1 = $this->group($a);
            $g2 = $this->group($c);
            if ($g1 !== $g2) return $g1 <=> $g2;
            if ($g1 === 0) return $c[0] <=> $a[0];
            if ($g1 === 1) {
                if ($a[0] !== $c[0]) return $c[0] <=> $a[0];
                return $a[1] <=> $c[1];
            }
            return $a[1] <=> $c[1];
        });
        $p = [];
        $p[0] = 1;
        for ($i = 1; $i < $b; $i++) $p[$i] = 2 * $p[$i - 1] % self::MOD;
        $ans = 0;
        $b--;
        foreach ($pairs as $pr) {
            $cnt1 = $pr[0];
            $cnt0 = $pr[1];
            while ($cnt1 > 0) {
                $ans = ($ans + $p[$b]) % self::MOD;
                $b--;
                $cnt1--;
            }
            $b -= $cnt0;
        }
        return $ans;
    }
}

<?php
// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

class Solution {
    function powerUpdate($nums, $p, $queries) {
        $L = [];
        $R = [];
        $sz1 = 0;
        $sz2 = count($nums);
        foreach ($nums as $x) $this->merge($R, $x, 1);
        $mod = 1000000007;
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $val = $queries[$qi][0];
            $k = $queries[$qi][1];
            $this->merge($R, $val, 1);
            $sz2++;
            $node = $this->firstKey($R);
            $this->merge($R, $node, -1);
            $sz2--;
            $this->merge($L, $node, 1);
            $sz1++;
            while ($sz2 < $k) {
                $node = $this->lastKey($L);
                $this->merge($L, $node, -1);
                $sz1--;
                $this->merge($R, $node, 1);
                $sz2++;
            }
            while ($sz2 > $k) {
                $node = $this->firstKey($R);
                $this->merge($R, $node, -1);
                $sz2--;
                $this->merge($L, $node, 1);
                $sz1++;
            }
            $x = $this->firstKey($R);
            $p = $this->qpow($p, $x, $mod);
            $ans[$qi] = $p;
        }
        return $ans;
    }

    private function merge(&$st, $x, $v) {
        $c = $st[$x] ?? 0;
        if ($c + $v === 0) unset($st[$x]);
        else $st[$x] = $c + $v;
    }

    private function firstKey($st) {
        $best = null;
        foreach ($st as $k => $_) {
            if ($best === null || $k < $best) $best = $k;
        }
        return $best;
    }

    private function lastKey($st) {
        $best = null;
        foreach ($st as $k => $_) {
            if ($best === null || $k > $best) $best = $k;
        }
        return $best;
    }

    private function qpow($a, $b, $mod) {
        $ans = 1;
        $a = $a % $mod;
        while ($b > 0) {
            if (($b & 1) !== 0) $ans = ($ans * $a) % $mod;
            $a = ($a * $a) % $mod;
            $b >>= 1;
        }
        return $ans;
    }
}

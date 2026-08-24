<?php
// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

class Solution {
    function powerUpdate($nums, $p, $queries) {
        $mod = 1000000007;
        $vals = $nums;
        foreach ($queries as $q) $vals[] = $q[0];
        sort($vals);
        $uniq = [];
        foreach ($vals as $v) {
            if (empty($uniq) || $v != $uniq[count($uniq) - 1]) $uniq[] = $v;
        }
        $vals = $uniq;
        $bit = array_fill(0, count($vals) + 1, 0);
        foreach ($nums as $x) $this->add($bit, $this->lowerBound($vals, $x) + 1);
        $ans = array_fill(0, count($queries), 0);
        $size = count($nums);
        $cur = $p;
        for ($i = 0; $i < count($queries); $i++) {
            $this->add($bit, $this->lowerBound($vals, $queries[$i][0]) + 1);
            $size++;
            $x = $this->kth($bit, $vals, $size - $queries[$i][1] + 1);
            $cur = $this->powm($cur, $x, $mod);
            $ans[$i] = $cur;
        }
        return $ans;
    }

    private function add(&$bit, $i) {
        $n = count($bit);
        for (; $i < $n; $i += $i & -$i) $bit[$i]++;
    }

    private function kth($bit, $vals, $rank) {
        $idx = 0;
        $step = 1;
        while (($step << 1) < count($bit)) $step <<= 1;
        for (; $step > 0; $step >>= 1) {
            $next = $idx + $step;
            if ($next < count($bit) && $bit[$next] < $rank) {
                $idx = $next;
                $rank -= $bit[$next];
            }
        }
        return $vals[$idx];
    }

    private function lowerBound($vals, $x) {
        $lo = 0;
        $hi = count($vals);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($vals[$mid] < $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function powm($a, $e, $mod) {
        $res = 1;
        while ($e > 0) {
            if (($e & 1) != 0) $res = ($res * $a) % $mod;
            $a = ($a * $a) % $mod;
            $e >>= 1;
        }
        return $res;
    }
}

<?php
// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

class Solution {
    function maximumScore($nums, $k) {
        $MOD = 1000000007;
        $n = count($nums);
        $maxV = 0;
        foreach ($nums as $v) $maxV = max($maxV, $v);
        $spf = array_fill(0, $maxV + 1, 0);
        for ($i = 2; $i <= $maxV; $i++) {
            if ($spf[$i] === 0) {
                for ($j = $i; $j <= $maxV; $j += $i) if ($spf[$j] === 0) $spf[$j] = $i;
            }
        }
        $primeScore = function($x) use ($spf) {
            $seen = [];
            while ($x > 1) {
                $p = $spf[$x];
                $seen[$p] = true;
                while ($x % $p === 0) $x = intdiv($x, $p);
            }
            return count($seen);
        };
        $score = [];
        foreach ($nums as $v) $score[] = $primeScore($v);
        $left = array_fill(0, $n, -1);
        $right = array_fill(0, $n, $n);
        $st = [];
        for ($i = 0; $i < $n; $i++) {
            while ($st && $score[$st[count($st) - 1]] < $score[$i]) array_pop($st);
            $left[$i] = $st ? $st[count($st) - 1] : -1;
            $st[] = $i;
        }
        $st = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while ($st && $score[$st[count($st) - 1]] <= $score[$i]) array_pop($st);
            $right[$i] = $st ? $st[count($st) - 1] : $n;
            $st[] = $i;
        }
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums[$i], ($i - $left[$i]) * ($right[$i] - $i)];
        usort($arr, function($a, $b) { return $b[0] <=> $a[0]; });
        $modPow = function($a, $b) use ($MOD) {
            $res = 1;
            $base = $a % $MOD;
            $exp = $b;
            while ($exp > 0) {
                if ($exp % 2 === 1) $res = ($res * $base) % $MOD;
                $base = ($base * $base) % $MOD;
                $exp = intdiv($exp, 2);
            }
            return $res;
        };
        $ans = 1;
        $remain = $k;
        foreach ($arr as $item) {
            if ($remain <= 0) break;
            $use = $item[1] < $remain ? $item[1] : $remain;
            $ans = $ans * $modPow($item[0], $use) % $MOD;
            $remain -= $use;
        }
        return $ans;
    }
}

<?php
// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

class Solution {
    private static $spf = null;

    private function primesOf($x) {
        $primes = [];
        while ($x > 1) {
            $p = self::$spf[$x];
            $primes[$p] = true;
            while ($x % $p === 0) $x = intdiv($x, $p);
        }
        return array_keys($primes);
    }

    function minJumps($nums) {
        $MX = 1000001;
        if (self::$spf === null) {
            $spf = array_fill(0, $MX, 0);
            for ($i = 2; $i < $MX; $i++) {
                if ($spf[$i] === 0) {
                    for ($j = $i; $j < $MX; $j += $i)
                        if ($spf[$j] === 0) $spf[$j] = $i;
                }
            }
            self::$spf = $spf;
        }
        $n = count($nums);
        $g = [];
        for ($i = 0; $i < $n; $i++) {
            foreach ($this->primesOf($nums[$i]) as $p) {
                if (!isset($g[$p])) $g[$p] = [];
                $g[$p][] = $i;
            }
        }
        $ans = 0;
        $vis = array_fill(0, $n, false);
        $vis[0] = true;
        $q = [0];
        while (true) {
            $nq = [];
            foreach ($q as $i) {
                if ($i === $n - 1) return $ans;
                $idx = isset($g[$nums[$i]]) ? $g[$nums[$i]] : [];
                $idx[] = $i + 1;
                if ($i > 0) $idx[] = $i - 1;
                foreach ($idx as $j) {
                    if ($j >= 0 && $j < $n && !$vis[$j]) {
                        $vis[$j] = true;
                        $nq[] = $j;
                    }
                }
                $g[$nums[$i]] = [];
            }
            $q = $nq;
            $ans++;
        }
    }
}

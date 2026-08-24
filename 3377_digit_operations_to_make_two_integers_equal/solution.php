<?php
// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

class Solution {
    function sieve($n) {
        $isP = array_fill(0, $n, false);
        for ($i = 2; $i < $n; $i++) $isP[$i] = true;
        for ($i = 2; $i * $i < $n; $i++) {
            if ($isP[$i]) {
                for ($j = $i * $i; $j < $n; $j += $i) $isP[$j] = false;
            }
        }
        return $isP;
    }

    function minOperations($n, $m) {
        $isPrime = $this->sieve(100000);
        if ($isPrime[$n]) return -1;
        $dist = array_fill(0, 100000, -1);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $pq->insert([$n, $n], -$n);
        $dist[$n] = $n;
        while (!$pq->isEmpty()) {
            $cur = $pq->extract();
            $cost = $cur[0];
            $val = $cur[1];
            if ($cost !== $dist[$val]) continue;
            if ($val === $m) return $cost;
            $s = str_split(strval($val));
            $len = count($s);
            for ($i = 0; $i < $len; $i++) {
                $orig = $s[$i];
                foreach ([-1, 1] as $d) {
                    $nd = (ord($orig) - 48) + $d;
                    if ($nd < 0 || $nd > 9) continue;
                    if ($i === 0 && $nd === 0 && $len > 1) continue;
                    $s[$i] = strval($nd);
                    $nv = intval(implode('', $s));
                    $s[$i] = $orig;
                    if ($isPrime[$nv]) continue;
                    $nc = $cost + $nv;
                    if ($dist[$nv] === -1 || $nc < $dist[$nv]) {
                        $dist[$nv] = $nc;
                        $pq->insert([$nc, $nv], -$nc);
                    }
                }
            }
        }
        return -1;
    }
}

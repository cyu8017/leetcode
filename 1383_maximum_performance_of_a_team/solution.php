<?php
class Solution {
    function maxPerformance($n, $speed, $efficiency, $k) {
        $pairs = [];
        for ($i = 0; $i < $n; $i++) $pairs[] = [$efficiency[$i], $speed[$i]];
        usort($pairs, function($a, $b) { return $b[0] <=> $a[0]; });
        $h = new SplMinHeap();
        $total = 0;
        $ans = 0;
        foreach ($pairs as [$e, $s]) {
            $h->insert($s);
            $total += $s;
            if ($h->count() > $k) $total -= $h->extract();
            $ans = max($ans, $total * $e);
        }
        return $ans % 1000000007;
    }
}

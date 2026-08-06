<?php
class Solution {
    function kWeakestRows($mat, $k) {
        $idx = range(0, count($mat) - 1);
        usort($idx, function($i, $j) use ($mat) {
            $si = array_sum($mat[$i]);
            $sj = array_sum($mat[$j]);
            if ($si !== $sj) return $si <=> $sj;
            return $i <=> $j;
        });
        return array_slice($idx, 0, $k);
    }
}

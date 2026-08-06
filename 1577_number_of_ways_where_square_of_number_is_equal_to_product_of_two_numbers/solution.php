<?php

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function numTriplets($nums1, $nums2) {
        return $this->count($nums1, $nums2) + $this->count($nums2, $nums1);
    }

    /**
     * @param Integer[] $a
     * @param Integer[] $b
     * @return Integer
     */
    private function count($a, $b) {
        $squares = [];
        foreach ($a as $x) {
            $sq = $x * $x;
            $squares[$sq] = ($squares[$sq] ?? 0) + 1;
        }
        $products = [];
        $n = count($b);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $p = $b[$i] * $b[$j];
                $products[$p] = ($products[$p] ?? 0) + 1;
            }
        }
        $total = 0;
        foreach ($squares as $value => $cnt) {
            $total += $cnt * ($products[$value] ?? 0);
        }
        return $total;
    }
}

<?php
// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

class Solution {
    function meltTable($report) {
        $out = [];
        foreach ($report as $r) {
            if (is_array($r) && isset($r[0]) && !isset($r['product'])) {
                $product = $r[0];
                for ($q = 1; $q <= 4; $q++) {
                    $out[] = ['product' => $product, 'quarter' => 'quarter_' . $q, 'sales' => $r[$q]];
                }
            } else {
                foreach (['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'] as $q) {
                    $out[] = ['product' => $r['product'], 'quarter' => $q, 'sales' => $r[$q]];
                }
            }
        }
        return $out;
    }
}

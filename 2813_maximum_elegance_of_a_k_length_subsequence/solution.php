<?php
// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

class Solution {
    function findMaximumElegance($items, $k) {
        usort($items, function($a, $b) { return $b[0] <=> $a[0]; });
        $seen = [];
        $total = 0;
        $dup = [];
        for ($i = 0; $i < $k; $i++) {
            $total += $items[$i][0];
            $c = $items[$i][1];
            if (isset($seen[$c])) $dup[] = $items[$i][0];
            else $seen[$c] = true;
        }
        $ans = $total + count($seen) * count($seen);
        for ($i = $k; $i < count($items); $i++) {
            $c = $items[$i][1];
            if (isset($seen[$c]) || !$dup) continue;
            $total += $items[$i][0] - array_pop($dup);
            $seen[$c] = true;
            $ans = max($ans, $total + count($seen) * count($seen));
        }
        return $ans;
    }
}

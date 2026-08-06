<?php
// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

class Solution {
    function maxDepthBST($order) {
        $nodes = []; // sorted [value, depth]
        $ans = 0;
        foreach ($order as $value) {
            $i = $this->bisectLeft($nodes, $value);
            $depth = 1;
            if ($i > 0) {
                $depth = max($depth, $nodes[$i - 1][1] + 1);
            }
            if ($i < count($nodes)) {
                $depth = max($depth, $nodes[$i][1] + 1);
            }
            array_splice($nodes, $i, 0, [[$value, $depth]]);
            $ans = max($ans, $depth);
        }
        return $ans;
    }

    private function bisectLeft($nodes, $value) {
        $lo = 0;
        $hi = count($nodes);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($nodes[$mid][0] < $value) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        return $lo;
    }
}

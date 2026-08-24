<?php
// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

class Solution {
    function maxProduct($nums) {
        $a = $nums;
        sort($a);
        $n = count($a);
        $A = $a[0]; $B = $a[1]; $C = $a[$n - 2]; $D = $a[$n - 1];
        $x = 100000;
        return max(max($A * $B * $x, $C * $D * $x), -$A * $D * $x);
    }
}

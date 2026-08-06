<?php
class Solution {
    function countOrders($n) {
        $ans = 1;
        $mod = 1000000007;
        for ($i = 1; $i <= $n; $i++) $ans = $ans * $i * (2 * $i - 1) % $mod;
        return $ans;
    }
}

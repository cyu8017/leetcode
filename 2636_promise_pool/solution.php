<?php
// LeetCode 2636 - Promise Pool
// https://leetcode.com/problems/promise-pool/

class Solution {
    function promisePool($functions, $n) {
        $i = 0;
        $len = count($functions);
        $worker = function() use (&$i, $functions, $len) {
            while ($i < $len) {
                $cur = $i++;
                $functions[$cur]();
            }
        };
        $limit = min($n, $len);
        for ($k = 0; $k < $limit; $k++) $worker();
        return null;
    }
}

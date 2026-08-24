<?php
// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

class Solution {
    function promiseAll($functions) {
        $n = count($functions);
        if ($n === 0) return [];
        $ans = array_fill(0, $n, null);
        for ($i = 0; $i < $n; $i++) $ans[$i] = $functions[$i]();
        return $ans;
    }
}

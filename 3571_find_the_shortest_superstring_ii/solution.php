<?php
// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

class Solution {
    function shortestSuperstring($s1, $s2) {
        if (strlen($s1) > strlen($s2)) return $this->shortestSuperstring($s2, $s1);
        $m = strlen($s1);
        if (strpos($s2, $s1) !== false) return $s2;
        for ($i = 0; $i < $m; $i++) {
            if (str_starts_with($s2, substr($s1, $i))) return substr($s1, 0, $i) . $s2;
            $len = $m - $i;
            if (strlen($s2) >= $len && substr($s2, -$len) === substr($s1, 0, $len))
                return $s2 . substr($s1, $m - $i);
        }
        return $s1 . $s2;
    }
}

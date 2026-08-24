<?php
// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
    function minimumString($a, $b, $c) {
        $merge = function($x, $y) {
            if (strpos($x, $y) !== false) return $x;
            $best = $x . $y;
            $n = min(strlen($x), strlen($y));
            for ($i = $n; $i > 0; $i--) {
                if (substr($x, -$i) === substr($y, 0, $i)) {
                    $cand = $x . substr($y, $i);
                    if (strlen($cand) < strlen($best) || (strlen($cand) === strlen($best) && $cand < $best)) $best = $cand;
                    break;
                }
            }
            return $best;
        };
        $perms = [[$a,$b,$c],[$a,$c,$b],[$b,$a,$c],[$b,$c,$a],[$c,$a,$b],[$c,$b,$a]];
        $ans = '';
        foreach ($perms as $p) {
            $cur = $merge($merge($p[0], $p[1]), $p[2]);
            if ($ans === '' || strlen($cur) < strlen($ans) || (strlen($cur) === strlen($ans) && $cur < $ans)) $ans = $cur;
        }
        return $ans;
    }
}

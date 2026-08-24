<?php
// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

class Solution {
    function knightDialer($n) {
        $MOD = 1000000007;
        $hops = [
            [4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
            [], [0, 1, 7], [2, 6], [1, 3], [2, 4]
        ];
        $dp = array_fill(0, 10, 1);
        for ($step = 1; $step < $n; $step++) {
            $next = array_fill(0, 10, 0);
            for ($d = 0; $d < 10; $d++) {
                foreach ($hops[$d] as $to) $next[$to] = ($next[$to] + $dp[$d]) % $MOD;
            }
            $dp = $next;
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $MOD;
        return $ans;
    }
}

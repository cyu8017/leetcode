<?php
// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

class Solution {
    /**
     * @param String $s
     * @param Integer $minJump
     * @param Integer $maxJump
     * @return Boolean
     */
    function canReach($s, $minJump, $maxJump) {
        $n = strlen($s);
        $reachable = array_fill(0, $n, false);
        $reachable[0] = true;
        $prefix = array_fill(0, $n + 1, 0);

        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && $s[$i] === '0') {
                $left = max(0, $i - $maxJump);
                $right = $i - $minJump;
                if ($right >= $left && $prefix[$right + 1] - $prefix[$left] > 0) {
                    $reachable[$i] = true;
                }
            }
            $prefix[$i + 1] = $prefix[$i] + ($reachable[$i] ? 1 : 0);
        }

        return $reachable[$n - 1];
    }
}

<?php
// LeetCode 1690 - Stone Game VII
// https://leetcode.com/problems/stone-game-vii/

class Solution {
    function stoneGameVII($stones) {
        $n = count($stones);
        $pre = [0];
        foreach ($stones as $x) $pre[] = $pre[count($pre) - 1] + $x;
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($length = 2; $length <= $n; $length++) {
            for ($i = 0; $i <= $n - $length; $i++) {
                $j = $i + $length - 1;
                $dp[$i][$j] = max($pre[$j + 1] - $pre[$i + 1] - $dp[$i + 1][$j], $pre[$j] - $pre[$i] - $dp[$i][$j - 1]);
            }
        }
        return $dp[0][$n - 1];
    }
}

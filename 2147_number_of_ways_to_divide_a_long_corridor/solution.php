<?php
// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution {
    /**
     * @param String $corridor
     * @return Integer
     */
    function numberOfWays($corridor) {
        $MOD = 1000000007;
        $seats = [];
        $n = strlen($corridor);
        for ($i = 0; $i < $n; $i++)
            if ($corridor[$i] === 'S') $seats[] = $i;
        if (count($seats) === 0 || count($seats) % 2 !== 0) return 0;
        $ans = 1;
        for ($i = 2; $i < count($seats); $i += 2)
            $ans = $ans * ($seats[$i] - $seats[$i - 1]) % $MOD;
        return $ans;
    }
}

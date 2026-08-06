<?php
class Solution {
    function numberWays($hats) {
        $mod = 1000000007;
        $people = count($hats);
        $wearers = array_fill(0, 41, []);
        foreach ($hats as $person => $choices) {
            foreach ($choices as $hat) $wearers[$hat][] = $person;
        }
        $dp = array_fill(0, 1 << $people, 0);
        $dp[0] = 1;
        for ($hat = 1; $hat <= 40; $hat++) {
            $nxt = $dp;
            foreach ($dp as $mask => $ways) {
                foreach ($wearers[$hat] as $person) {
                    if ((($mask >> $person) & 1) === 0) {
                        $nxt[$mask | (1 << $person)] = ($nxt[$mask | (1 << $person)] + $ways) % $mod;
                    }
                }
            }
            $dp = $nxt;
        }
        return $dp[(1 << $people) - 1];
    }
}

<?php
// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

class Solution {
    /**
     * @param Integer $n
     * @param Integer $minProfit
     * @param Integer[] $group
     * @param Integer[] $profit
     * @return Integer
     */
    function profitableSchemes($n, $minProfit, $group, $profit) {
        $MOD = 1000000007;
        $dp = array_fill(0, $n + 1, array_fill(0, $minProfit + 1, 0));
        $dp[0][0] = 1;
        $gn = count($group);
        for ($i = 0; $i < $gn; $i++) {
            $members = $group[$i];
            $p = $profit[$i];
            for ($people = $n; $people >= $members; $people--) {
                for ($prof = $minProfit; $prof >= 0; $prof--) {
                    $np = min($minProfit, $prof + $p);
                    $dp[$people][$np] = ($dp[$people][$np] + $dp[$people - $members][$prof]) % $MOD;
                }
            }
        }
        $ans = 0;
        for ($people = 0; $people <= $n; $people++) $ans = ($ans + $dp[$people][$minProfit]) % $MOD;
        return $ans;
    }
}

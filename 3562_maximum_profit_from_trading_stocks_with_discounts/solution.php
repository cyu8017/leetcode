<?php
// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

class Solution {
    private $g;
    private $present;
    private $future;
    private $budget;

    private function dfs($u) {
        $nxt = [];
        for ($j = 0; $j <= $this->budget; $j++) $nxt[$j] = [0, 0];
        foreach ($this->g[$u] as $v) {
            $fv = $this->dfs($v);
            for ($j = $this->budget; $j >= 0; $j--) {
                for ($jv = 0; $jv <= $j; $jv++) {
                    for ($pre = 0; $pre < 2; $pre++) {
                        $nxt[$j][$pre] = max($nxt[$j][$pre], $nxt[$j - $jv][$pre] + $fv[$jv][$pre]);
                    }
                }
            }
        }
        $f = [];
        for ($j = 0; $j <= $this->budget; $j++) $f[$j] = [0, 0];
        $price = $this->future[$u - 1];
        for ($j = 0; $j <= $this->budget; $j++) {
            for ($pre = 0; $pre < 2; $pre++) {
                $cost = intdiv($this->present[$u - 1], $pre + 1);
                if ($j >= $cost) {
                    $buyProfit = $nxt[$j - $cost][1] + ($price - $cost);
                    $f[$j][$pre] = max($nxt[$j][0], $buyProfit);
                } else {
                    $f[$j][$pre] = $nxt[$j][0];
                }
            }
        }
        return $f;
    }

    function maxProfit($n, $present, $future, $hierarchy, $budget) {
        $this->g = array_fill(0, $n + 1, []);
        foreach ($hierarchy as $e) $this->g[$e[0]][] = $e[1];
        $this->present = $present;
        $this->future = $future;
        $this->budget = $budget;
        return $this->dfs(1)[$budget][0];
    }
}

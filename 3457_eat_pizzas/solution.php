<?php
// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

class Solution {
    function maxWeight($pizzas) {
        sort($pizzas);
        $n = count($pizzas);
        $days = intdiv($n, 4);
        $ans = 0;
        $oddDays = intdiv($days + 1, 2);
        $evenDays = intdiv($days, 2);
        $idx = $n - 1;
        for ($i = 0; $i < $oddDays; $i++) {
            $ans += $pizzas[$idx];
            $idx--;
        }
        for ($i = 0; $i < $evenDays; $i++) {
            $idx--;
            $ans += $pizzas[$idx];
            $idx--;
        }
        return $ans;
    }
}

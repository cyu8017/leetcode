<?php
// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

class Solution {
    function maxItems($items, $budget) {
        $n = count($items);
        $frequency = array_fill(0, $n + 1, 0);
        $minimumPrice = $items[0][1];
        foreach ($items as $item) {
            $frequency[$item[0]]++;
            $minimumPrice = min($minimumPrice, $item[1]);
        }
        $batches = [];
        foreach ($items as $item) {
            $gain = 0;
            for ($multiple = $item[0]; $multiple <= $n; $multiple += $item[0]) $gain += $frequency[$multiple];
            $gain--;
            if ($gain > 0 && $item[1] < 2 * $minimumPrice) $batches[] = [$item[1], $gain];
        }
        usort($batches, function ($a, $b) { return $a[0] <=> $b[0]; });
        $remaining = $budget;
        $answer = intdiv($budget, $minimumPrice);
        $boosted = 0;
        foreach ($batches as $current) {
            $count = $current[1];
            $affordable = intdiv($remaining, $current[0]);
            if ($affordable < $count) $count = $affordable;
            $remaining -= $count * $current[0];
            $boosted += $count;
            $total = 2 * $boosted + intdiv($remaining, $minimumPrice);
            if ($total > $answer) $answer = $total;
            if ($count < $current[1]) break;
        }
        return $answer;
    }
}

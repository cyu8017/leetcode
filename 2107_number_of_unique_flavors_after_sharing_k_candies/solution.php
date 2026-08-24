<?php
// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

class Solution {
    /**
     * @param Integer[] $candies
     * @param Integer $k
     * @return Integer
     */
    function shareCandies($candies, $k) {
        $n = count($candies);
        $freq = [];
        foreach ($candies as $c) $freq[$c] = ($freq[$c] ?? 0) + 1;
        if ($k === 0) return count($freq);
        for ($i = 0; $i < $k; $i++) {
            $c = $candies[$i];
            $v = $freq[$c] - 1;
            if ($v === 0) unset($freq[$c]);
            else $freq[$c] = $v;
        }
        $ans = count($freq);
        for ($i = $k; $i < $n; $i++) {
            $freq[$candies[$i - $k]] = ($freq[$candies[$i - $k]] ?? 0) + 1;
            $c = $candies[$i];
            $v = $freq[$c] - 1;
            if ($v === 0) unset($freq[$c]);
            else $freq[$c] = $v;
            $ans = max($ans, count($freq));
        }
        return $ans;
    }
}

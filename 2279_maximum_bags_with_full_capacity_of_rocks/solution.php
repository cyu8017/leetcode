<?php
// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution {
    function maximumBags($capacity, $rocks, $additionalRocks) {
        $need = [];
        for ($i = 0; $i < count($capacity); $i++) $need[] = $capacity[$i] - $rocks[$i];
        sort($need);
        $ans = 0;
        foreach ($need as $n) {
            if ($additionalRocks < $n) break;
            $additionalRocks -= $n;
            $ans++;
        }
        return $ans;
    }
}

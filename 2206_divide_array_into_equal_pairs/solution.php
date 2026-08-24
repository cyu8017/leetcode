<?php
// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution {
    function divideArray($nums) {
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        foreach ($freq as $c) if ($c % 2 !== 0) return false;
        return true;
    }
}

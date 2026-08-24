<?php
// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

class Solution {
    function numJewelsInStones($jewels, $stones) {
        $jewelSet = [];
        $jlen = strlen($jewels);
        for ($i = 0; $i < $jlen; $i++) $jewelSet[$jewels[$i]] = true;
        $count = 0;
        $slen = strlen($stones);
        for ($i = 0; $i < $slen; $i++) if (isset($jewelSet[$stones[$i]])) $count++;
        return $count;
    }
}

<?php
// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

class Solution {
    function beautifulArray($n) {
        $res = [1];
        while (count($res) < $n) {
            $tmp = [];
            foreach ($res as $x) if ($x * 2 - 1 <= $n) $tmp[] = $x * 2 - 1;
            foreach ($res as $x) if ($x * 2 <= $n) $tmp[] = $x * 2;
            $res = $tmp;
        }
        return $res;
    }
}

<?php
// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

class Solution {
    function oddEvenJumps($arr) {
        $n = count($arr);
        $nextHigher = array_fill(0, $n, 0);
        $nextLower = array_fill(0, $n, 0);
        $order = range(0, $n - 1);
        usort($order, function ($i, $j) use ($arr) {
            return $arr[$i] === $arr[$j] ? $i <=> $j : $arr[$i] <=> $arr[$j];
        });
        $stack = [];
        foreach ($order as $i) {
            while ($stack && $stack[count($stack) - 1] < $i) {
                $nextHigher[$stack[count($stack) - 1]] = $i;
                array_pop($stack);
            }
            $stack[] = $i;
        }
        $stack = [];
        usort($order, function ($i, $j) use ($arr) {
            return $arr[$i] === $arr[$j] ? $i <=> $j : $arr[$j] <=> $arr[$i];
        });
        foreach ($order as $i) {
            while ($stack && $stack[count($stack) - 1] < $i) {
                $nextLower[$stack[count($stack) - 1]] = $i;
                array_pop($stack);
            }
            $stack[] = $i;
        }
        $odd = array_fill(0, $n, false);
        $even = array_fill(0, $n, false);
        $odd[$n - 1] = true;
        $even[$n - 1] = true;
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($nextHigher[$i] !== 0) $odd[$i] = $even[$nextHigher[$i]];
            if ($nextLower[$i] !== 0) $even[$i] = $odd[$nextLower[$i]];
        }
        $ans = 0;
        foreach ($odd as $x) if ($x) $ans++;
        return $ans;
    }
}

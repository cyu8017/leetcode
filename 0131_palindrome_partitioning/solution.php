<?php

class Solution {
    function partition($s) {
        $result = [];
        $path = [];
        $n = strlen($s);

        $isPalindrome = function ($left, $right) use ($s) {
            while ($left < $right) {
                if ($s[$left] !== $s[$right]) {
                    return false;
                }
                $left++;
                $right--;
            }
            return true;
        };

        $dfs = function ($start) use (&$dfs, &$result, &$path, $n, $s, $isPalindrome) {
            if ($start === $n) {
                $result[] = $path;
                return;
            }
            for ($end = $start; $end < $n; $end++) {
                if ($isPalindrome($start, $end)) {
                    $path[] = substr($s, $start, $end - $start + 1);
                    $dfs($end + 1);
                    array_pop($path);
                }
            }
        };

        $dfs(0);
        return $result;
    }
}
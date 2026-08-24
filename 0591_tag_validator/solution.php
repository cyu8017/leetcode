<?php
// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

class Solution {
    function isValid($code) {
        $stack = [];
        $i = 0;
        $n = strlen($code);
        while ($i < $n) {
            if (substr($code, $i, 9) === "<![CDATA[") {
                if (!$stack) return false;
                $j = strpos($code, "]]>", $i + 9);
                if ($j === false) return false;
                $i = $j + 3;
            } elseif (substr($code, $i, 2) === "</") {
                $j = strpos($code, ">", $i + 2);
                if ($j === false) return false;
                $tag = substr($code, $i + 2, $j - ($i + 2));
                if (!$stack || $stack[count($stack) - 1] !== $tag) return false;
                array_pop($stack);
                $i = $j + 1;
                if (!$stack && $i < $n) return false;
            } elseif ($code[$i] === "<") {
                $j = strpos($code, ">", $i + 1);
                if ($j === false) return false;
                $tag = substr($code, $i + 1, $j - ($i + 1));
                if ($tag === "" || strlen($tag) > 9) return false;
                for ($k = 0; $k < strlen($tag); ++$k) {
                    $ch = ord($tag[$k]);
                    if ($ch < 65 || $ch > 90) return false;
                }
                $stack[] = $tag;
                $i = $j + 1;
            } else {
                if (!$stack) return false;
                ++$i;
            }
        }
        return count($stack) === 0;
    }
}

<?php
// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

class Solution {
    function removeComments($source) {
        $result = [];
        $buffer = '';
        $inBlock = false;
        foreach ($source as $line) {
            $i = 0;
            $len = strlen($line);
            while ($i < $len) {
                if ($inBlock) {
                    if ($i + 1 < $len && $line[$i] === '*' && $line[$i + 1] === '/') {
                        $inBlock = false;
                        $i += 2;
                    } else $i++;
                } else if ($i + 1 < $len && $line[$i] === '/' && $line[$i + 1] === '*') {
                    $inBlock = true;
                    $i += 2;
                } else if ($i + 1 < $len && $line[$i] === '/' && $line[$i + 1] === '/') break;
                else $buffer .= $line[$i++];
            }
            if (!$inBlock && strlen($buffer) > 0) {
                $result[] = $buffer;
                $buffer = '';
            }
        }
        return $result;
    }
}

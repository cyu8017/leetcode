<?php
// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

class InfiniteStream {
    private $bits;
    private $i = 0;
    function __construct($bits) {
        $this->bits = [];
        foreach ($bits as $b) {
            if ($b === '...') continue;
            $this->bits[] = (int)$b;
        }
    }
    function next() {
        if ($this->i >= count($this->bits)) return 0;
        return $this->bits[$this->i++];
    }
}

class Solution {
    function findPattern($stream, $pattern) {
        if (is_array($stream)) $stream = new InfiniteStream($stream);
        $a = 0;
        $b = 0;
        $m = count($pattern);
        $half = $m >> 1;
        $mask1 = (1 << $half) - 1;
        $mask2 = (1 << ($m - $half)) - 1;
        for ($i = 0; $i < $half; $i++) $a |= $pattern[$i] << ($half - 1 - $i);
        for ($i = $half; $i < $m; $i++) $b |= $pattern[$i] << ($m - 1 - $i);
        $x = 0;
        $y = 0;
        for ($i = 1; ; $i++) {
            $v = $stream->next();
            $y = $y << 1 | $v;
            $v = ($y >> ($m - $half)) & 1;
            $y &= $mask2;
            $x = $x << 1 | $v;
            $x &= $mask1;
            if ($i >= $m && $a === $x && $b === $y) return $i - $m;
        }
    }
}

<?php
// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

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
    private function getLPS($pattern) {
        $n = count($pattern);
        $lps = array_fill(0, $n, 0);
        $j = 0;
        for ($i = 1; $i < $n; $i++) {
            while ($j > 0 && $pattern[$j] !== $pattern[$i]) $j = $lps[$j - 1];
            if ($pattern[$i] === $pattern[$j]) {
                $j++;
                $lps[$i] = $j;
            }
        }
        return $lps;
    }

    function findPattern($stream, $pattern) {
        if (is_array($stream)) $stream = new InfiniteStream($stream);
        $lps = $this->getLPS($pattern);
        $i = 0;
        $j = 0;
        $bit = 0;
        $readNext = false;
        while (true) {
            if (!$readNext) {
                $bit = $stream->next();
                $readNext = true;
            }
            if ($bit === $pattern[$j]) {
                $i++;
                $readNext = false;
                $j++;
                if ($j === count($pattern)) return $i - $j;
            } else if ($j > 0) {
                $j = $lps[$j - 1];
            } else {
                $i++;
                $readNext = false;
            }
        }
    }
}

<?php
// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

class TrieNode {
    public $count = 0;
    /** @var array<int, TrieNode|null> */
    public $children = [null, null];
}

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countPairs($nums, $low, $high) {
        return $this->countSmallerThan($nums, $high + 1) - $this->countSmallerThan($nums, $low);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer
     */
    private function countSmallerThan($nums, $limit) {
        if ($limit <= 0) {
            return 0;
        }

        $root = new TrieNode();
        $total = 0;
        $maxBit = 15;

        foreach ($nums as $num) {
            $total += $this->query($root, $num, $limit, $maxBit);
            $this->insert($root, $num, $maxBit);
        }
        return $total;
    }

    private function insert($root, $num, $bit) {
        $node = $root;
        for ($i = $bit; $i >= 0; $i--) {
            $b = ($num >> $i) & 1;
            if ($node->children[$b] === null) {
                $node->children[$b] = new TrieNode();
            }
            $node = $node->children[$b];
            $node->count++;
        }
    }

    private function query($root, $num, $limit, $bit) {
        if ($root === null || $bit < 0) {
            return 0;
        }

        $numBit = ($num >> $bit) & 1;
        $limitBit = ($limit >> $bit) & 1;
        $child = $root->children[$numBit];

        if ($limitBit === 1) {
            $result = $child !== null ? $child->count : 0;
            $result += $this->query($root->children[1 - $numBit], $num, $limit, $bit - 1);
            return $result;
        }
        return $this->query($child, $num, $limit, $bit - 1);
    }
}

<?php
// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class SORTracker {
    private $best = [];
    private $rest = [];
    private $k = 0;

    function __construct() {
        $this->best = [];
        $this->rest = [];
        $this->k = 0;
    }

    private function cmpBest($a, $b) {
        if ($a['score'] !== $b['score']) return $a['score'] - $b['score'];
        if ($b['name'] < $a['name']) return -1;
        if ($b['name'] > $a['name']) return 1;
        return 0;
    }

    private function cmpRest($a, $b) {
        if ($a['score'] !== $b['score']) return $b['score'] - $a['score'];
        if ($a['name'] < $b['name']) return -1;
        if ($a['name'] > $b['name']) return 1;
        return 0;
    }

    private function heapPush(&$heap, $item, $cmp) {
        $heap[] = $item;
        $i = count($heap) - 1;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($this->$cmp($heap[$p], $heap[$i]) <= 0) break;
            $t = $heap[$p];
            $heap[$p] = $heap[$i];
            $heap[$i] = $t;
            $i = $p;
        }
    }

    private function heapPop(&$heap, $cmp) {
        $top = $heap[0];
        $last = array_pop($heap);
        if ($heap) {
            $heap[0] = $last;
            $i = 0;
            $n = count($heap);
            while (true) {
                $l = $i * 2 + 1;
                $r = $l + 1;
                $s = $i;
                if ($l < $n && $this->$cmp($heap[$l], $heap[$s]) < 0) $s = $l;
                if ($r < $n && $this->$cmp($heap[$r], $heap[$s]) < 0) $s = $r;
                if ($s === $i) break;
                $t = $heap[$s];
                $heap[$s] = $heap[$i];
                $heap[$i] = $t;
                $i = $s;
            }
        }
        return $top;
    }

    /**
     * @param String $name
     * @param Integer $score
     * @return NULL
     */
    function add($name, $score) {
        $this->heapPush($this->best, ['name' => $name, 'score' => $score], 'cmpBest');
        if (count($this->best) > $this->k) {
            $this->heapPush($this->rest, $this->heapPop($this->best, 'cmpBest'), 'cmpRest');
        }
    }

    /**
     * @return String
     */
    function get() {
        $this->k++;
        if ($this->rest) $this->heapPush($this->best, $this->heapPop($this->rest, 'cmpRest'), 'cmpBest');
        return $this->best[0]['name'];
    }
}

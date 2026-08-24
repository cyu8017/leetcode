<?php
// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

class QueryBatcher {
    public $queryMultiple;
    public $t;
    public $pending = [];
    public $busyUntil = 0;
    function __construct($queryMultiple, $t) {
        $this->queryMultiple = $queryMultiple;
        $this->t = $t;
    }
    function getValue($key, $now = null) {
        if ($now === null) $now = (int)(microtime(true) * 1000);
        $this->pending[] = $key;
        if ($now >= $this->busyUntil) {
            return $this->flush($now);
        }
        return $this->pending;
    }
    function flush($now = null) {
        if (!$this->pending) return [];
        $batch = $this->pending;
        $this->pending = [];
        if ($now === null) $now = (int)(microtime(true) * 1000);
        $this->busyUntil = $now + $this->t;
        $fn = $this->queryMultiple;
        return $fn($batch);
    }
}

<?php
// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

class LFUCache {
    private int $capacity;
    private int $minFreq = 0;
    private array $keyValues = [];
    private array $keyFreqs = [];
    private array $freqKeys = [];

    function __construct(int $capacity) {
        $this->capacity = $capacity;
    }

    private function touch(int $key): void {
        $freq = $this->keyFreqs[$key];
        $bucket = &$this->freqKeys[$freq];
        $index = array_search($key, $bucket, true);
        if ($index !== false) {
            array_splice($bucket, $index, 1);
        }
        if (empty($bucket) && $freq === $this->minFreq) {
            $this->minFreq++;
        }
        $this->keyFreqs[$key] = $freq + 1;
        if (!array_key_exists($freq + 1, $this->freqKeys)) {
            $this->freqKeys[$freq + 1] = [];
        }
        $this->freqKeys[$freq + 1][] = $key;
    }

    function get(int $key): int {
        if (!array_key_exists($key, $this->keyValues)) {
            return -1;
        }
        $this->touch($key);
        return $this->keyValues[$key];
    }

    function put(int $key, int $value): void {
        if ($this->capacity === 0) {
            return;
        }
        if (array_key_exists($key, $this->keyValues)) {
            $this->keyValues[$key] = $value;
            $this->touch($key);
            return;
        }

        if (count($this->keyValues) >= $this->capacity) {
            $evict = array_shift($this->freqKeys[$this->minFreq]);
            unset($this->keyValues[$evict], $this->keyFreqs[$evict]);
        }

        $this->keyValues[$key] = $value;
        $this->keyFreqs[$key] = 1;
        if (!array_key_exists(1, $this->freqKeys)) {
            $this->freqKeys[1] = [];
        }
        $this->freqKeys[1][] = $key;
        $this->minFreq = 1;
    }
}

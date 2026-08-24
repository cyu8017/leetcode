<?php
// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache {
    private $data = [];

    function set($key, $value, $duration) {
        $now = (int)round(microtime(true) * 1000);
        $alive = isset($this->data[$key]) && $this->data[$key]['expire'] > $now;
        $this->data[$key] = ['value' => $value, 'expire' => $now + $duration];
        return $alive;
    }

    function get($key) {
        $now = (int)round(microtime(true) * 1000);
        if (!isset($this->data[$key]) || $this->data[$key]['expire'] <= $now) return -1;
        return $this->data[$key]['value'];
    }

    function count() {
        $now = (int)round(microtime(true) * 1000);
        $cnt = 0;
        foreach ($this->data as $k => $e) {
            if ($e['expire'] > $now) $cnt++;
            else unset($this->data[$k]);
        }
        return $cnt;
    }
}

class Solution {
    function TimeLimitedCache() {
        return new TimeLimitedCache();
    }
}

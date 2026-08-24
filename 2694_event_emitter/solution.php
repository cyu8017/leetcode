<?php
// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

class EventEmitter {
    private $handlers = [];

    function subscribe($eventName, $callback) {
        if (!isset($this->handlers[$eventName])) $this->handlers[$eventName] = [];
        $this->handlers[$eventName][] = $callback;
        $list =& $this->handlers[$eventName];
        return [
            'unsubscribe' => function() use (&$list, $callback) {
                $idx = array_search($callback, $list, true);
                if ($idx !== false) array_splice($list, $idx, 1);
            },
        ];
    }

    function emit($eventName, $args = []) {
        $list = $this->handlers[$eventName] ?? [];
        $out = [];
        foreach ($list as $cb) $out[] = $cb(...$args);
        return $out;
    }
}

class Solution {
    function EventEmitter($actions = null, $values = null) {
        return new EventEmitter();
    }
}

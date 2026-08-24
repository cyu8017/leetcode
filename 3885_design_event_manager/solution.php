<?php
// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

class EventManager {
    public $sl = [];
    public $d = [];
    function __construct($events) {
        $this->sl = [];
        $this->d = [];
        foreach ($events as $e) {
            $eventId = $e[0];
            $priority = $e[1];
            $this->sl[] = [-$priority, $eventId];
            $this->d[$eventId] = $priority;
        }
        $this->_sort();
    }
    function _sort() {
        usort($this->sl, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
    }
    function updatePriority($eventId, $newPriority) {
        $old = $this->d[$eventId];
        $this->sl = array_values(array_filter($this->sl, function($x) use ($old, $eventId) {
            return !($x[0] === -$old && $x[1] === $eventId);
        }));
        $this->sl[] = [-$newPriority, $eventId];
        $this->d[$eventId] = $newPriority;
        $this->_sort();
    }
    function pollHighest() {
        if (!count($this->sl)) return -1;
        $top = array_shift($this->sl);
        $eventId = $top[1];
        unset($this->d[$eventId]);
        return $eventId;
    }
}

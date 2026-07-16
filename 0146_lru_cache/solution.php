<?php

class Node {
    public int $key;
    public int $value;
    public ?Node $prev = null;
    public ?Node $next = null;

    function __construct(int $key = 0, int $value = 0) {
        $this->key = $key;
        $this->value = $value;
    }
}

class LRUCache {
    private int $capacity;
    private array $cache = [];
    private Node $head;
    private Node $tail;

    function __construct(int $capacity) {
        $this->capacity = $capacity;
        $this->head = new Node();
        $this->tail = new Node();
        $this->head->next = $this->tail;
        $this->tail->prev = $this->head;
    }

    private function remove(Node $node): void {
        $node->prev->next = $node->next;
        $node->next->prev = $node->prev;
    }

    private function addToFront(Node $node): void {
        $node->prev = $this->head;
        $node->next = $this->head->next;
        $this->head->next->prev = $node;
        $this->head->next = $node;
    }

    function get(int $key): int {
        if (!isset($this->cache[$key])) {
            return -1;
        }
        $node = $this->cache[$key];
        $this->remove($node);
        $this->addToFront($node);
        return $node->value;
    }

    function put(int $key, int $value): void {
        if (isset($this->cache[$key])) {
            $node = $this->cache[$key];
            $node->value = $value;
            $this->remove($node);
            $this->addToFront($node);
            return;
        }

        if (count($this->cache) === $this->capacity) {
            $leastRecent = $this->tail->prev;
            $this->remove($leastRecent);
            unset($this->cache[$leastRecent->key]);
        }

        $node = new Node($key, $value);
        $this->cache[$key] = $node;
        $this->addToFront($node);
    }
}
<?php
// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice {
    private $latestTs = 0;
    private $priceAt = [];
    private $maxHeap;
    private $minHeap;

    function __construct() {
        $this->maxHeap = new SplPriorityQueue();
        $this->minHeap = new SplPriorityQueue();
    }

    /**
     * @param Integer $timestamp
     * @param Integer $price
     * @return NULL
     */
    function update($timestamp, $price) {
        $this->priceAt[$timestamp] = $price;
        if ($timestamp >= $this->latestTs) $this->latestTs = $timestamp;
        $this->maxHeap->insert([$price, $timestamp], $price);
        $this->minHeap->insert([$price, $timestamp], -$price);
    }

    /**
     * @return Integer
     */
    function current() {
        return $this->priceAt[$this->latestTs];
    }

    /**
     * @return Integer
     */
    function maximum() {
        while (true) {
            $top = $this->maxHeap->top();
            if ($this->priceAt[$top[1]] === $top[0]) return $top[0];
            $this->maxHeap->extract();
        }
    }

    /**
     * @return Integer
     */
    function minimum() {
        while (true) {
            $top = $this->minHeap->top();
            if ($this->priceAt[$top[1]] === $top[0]) return $top[0];
            $this->minHeap->extract();
        }
    }
}

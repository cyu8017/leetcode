<?php
// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem {
    public $orderTypeMap;
    public $priceMap;
    public $t;
    function __construct() {
        $this->orderTypeMap = [];
        $this->priceMap = [];
        $this->t = [];
    }
    function _key($orderType, $price) {
        return $orderType . '#' . $price;
    }
    function addOrder($orderId, $orderType, $price) {
        $this->orderTypeMap[$orderId] = $orderType;
        $this->priceMap[$orderId] = $price;
        $key = $this->_key($orderType, $price);
        if (!isset($this->t[$key])) $this->t[$key] = [];
        $this->t[$key][] = $orderId;
    }
    function modifyOrder($orderId, $newPrice) {
        $orderType = $this->orderTypeMap[$orderId];
        $oldPrice = $this->priceMap[$orderId];
        $this->priceMap[$orderId] = $newPrice;
        $oldKey = $this->_key($orderType, $oldPrice);
        $oldList = &$this->t[$oldKey];
        for ($i = 0; $i < count($oldList); $i++) {
            if ($oldList[$i] === $orderId) {
                array_splice($oldList, $i, 1);
                break;
            }
        }
        $key = $this->_key($orderType, $newPrice);
        if (!isset($this->t[$key])) $this->t[$key] = [];
        $this->t[$key][] = $orderId;
    }
    function cancelOrder($orderId) {
        $orderType = $this->orderTypeMap[$orderId];
        $price = $this->priceMap[$orderId];
        unset($this->orderTypeMap[$orderId]);
        unset($this->priceMap[$orderId]);
        $key = $this->_key($orderType, $price);
        $list = &$this->t[$key];
        for ($i = 0; $i < count($list); $i++) {
            if ($list[$i] === $orderId) {
                array_splice($list, $i, 1);
                break;
            }
        }
    }
    function getOrdersAtPrice($orderType, $price) {
        $key = $this->_key($orderType, $price);
        if (!isset($this->t[$key])) return [];
        return $this->t[$key];
    }
}

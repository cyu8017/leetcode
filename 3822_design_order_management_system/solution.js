// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design_order_management_system/

var OrderManagementSystem = function() {
    this.orderTypeMap = new Map();
    this.priceMap = new Map();
    this.t = new Map();
};

OrderManagementSystem.prototype._key = function(orderType, price) {
    return orderType + '#' + price;
};

OrderManagementSystem.prototype.addOrder = function(orderId, orderType, price) {
    this.orderTypeMap.set(orderId, orderType);
    this.priceMap.set(orderId, price);
    const key = this._key(orderType, price);
    if (!this.t.has(key)) this.t.set(key, []);
    this.t.get(key).push(orderId);
};

OrderManagementSystem.prototype.modifyOrder = function(orderId, newPrice) {
    const orderType = this.orderTypeMap.get(orderId);
    const oldPrice = this.priceMap.get(orderId);
    this.priceMap.set(orderId, newPrice);
    const oldKey = this._key(orderType, oldPrice);
    const oldList = this.t.get(oldKey);
    for (let i = 0; i < oldList.length; i++) {
        if (oldList[i] === orderId) {
            oldList.splice(i, 1);
            break;
        }
    }
    const key = this._key(orderType, newPrice);
    if (!this.t.has(key)) this.t.set(key, []);
    this.t.get(key).push(orderId);
};

OrderManagementSystem.prototype.cancelOrder = function(orderId) {
    const orderType = this.orderTypeMap.get(orderId);
    const price = this.priceMap.get(orderId);
    this.orderTypeMap.delete(orderId);
    this.priceMap.delete(orderId);
    const key = this._key(orderType, price);
    const list = this.t.get(key);
    for (let i = 0; i < list.length; i++) {
        if (list[i] === orderId) {
            list.splice(i, 1);
            break;
        }
    }
};

OrderManagementSystem.prototype.getOrdersAtPrice = function(orderType, price) {
    const key = this._key(orderType, price);
    const list = this.t.get(key);
    if (!list) return [];
    return list.slice();
};

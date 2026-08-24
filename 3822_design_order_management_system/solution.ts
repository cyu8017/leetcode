// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design_order_management_system/

export class OrderManagementSystem {
    constructor() {
    this.orderTypeMap = new Map();
    this.priceMap = new Map();
    this.t = new Map();
}
    _key(orderType: any, price: any): any {
    return orderType + '#' + price;
}
    addOrder(orderId: any, orderType: any, price: any): any {
    this.orderTypeMap.set(orderId, orderType);
    this.priceMap.set(orderId, price);
    const key = this._key(orderType, price);
    if (!this.t.has(key)) this.t.set(key, []);
    this.t.get(key).push(orderId);
}
    modifyOrder(orderId: any, newPrice: any): any {
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
}
    cancelOrder(orderId: any): any {
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
}
    getOrdersAtPrice(orderType: any, price: any): any {
    const key = this._key(orderType, price);
    const list = this.t.get(key);
    if (!list) return [];
    return list.slice();
}
}

// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem {
    private var orderTypeMap = [Int: String]()
    private var priceMap = [Int: Int]()
    private var t = [String: [Int]]()

    private func key(_ orderType: String, _ price: Int) -> String {
        return "\(orderType)#\(price)"
    }

    init() {}

    func addOrder(_ orderId: Int, _ orderType: String, _ price: Int) {
        orderTypeMap[orderId] = orderType
        priceMap[orderId] = price
        t[key(orderType, price), default: []].append(orderId)
    }

    func modifyOrder(_ orderId: Int, _ newPrice: Int) {
        let orderType = orderTypeMap[orderId]!
        let oldPrice = priceMap[orderId]!
        priceMap[orderId] = newPrice
        let oldKey = key(orderType, oldPrice)
        if var oldList = t[oldKey] {
            if let i = oldList.firstIndex(of: orderId) { oldList.remove(at: i) }
            t[oldKey] = oldList
        }
        t[key(orderType, newPrice), default: []].append(orderId)
    }

    func cancelOrder(_ orderId: Int) {
        let orderType = orderTypeMap[orderId]!
        let price = priceMap[orderId]!
        orderTypeMap.removeValue(forKey: orderId)
        priceMap.removeValue(forKey: orderId)
        let k = key(orderType, price)
        if var list = t[k] {
            if let i = list.firstIndex(of: orderId) { list.remove(at: i) }
            t[k] = list
        }
    }

    func getOrdersAtPrice(_ orderType: String, _ price: Int) -> [Int] {
        return t[key(orderType, price)] ?? []
    }
}

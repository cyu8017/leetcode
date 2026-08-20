// LeetCode 1357 - Apply Discount Every n Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier {
    private let n: Int
    private let discount: Int
    private var price = [Int: Int]()
    private var count = 0

    init(_ n: Int, _ discount: Int, _ products: [Int], _ prices: [Int]) {
        self.n = n
        self.discount = discount
        for i in 0..<products.count { price[products[i]] = prices[i] }
    }

    func getBill(_ product: [Int], _ amount: [Int]) -> Double {
        count += 1
        var total = 0
        for i in 0..<product.count { total += price[product[i]]! * amount[i] }
        if count % n == 0 {
            return Double(total) * Double(100 - discount) / 100.0
        }
        return Double(total)
    }
}

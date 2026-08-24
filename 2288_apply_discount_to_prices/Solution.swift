// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

class Solution {
    func discountPrices(_ sentence: String, _ discount: Int) -> String {
        let parts = sentence.split(separator: " ", omittingEmptySubsequences: false).map { String($0) }
        return parts.map { part in
            if part.count >= 2 && part.first == "$" {
                let rest = String(part.dropFirst())
                if rest.allSatisfy({ $0.isNumber }) {
                    let val = Double(rest)!
                    let price = val * (100.0 - Double(discount)) / 100.0
                    return String(format: "$%.2f", price)
                }
            }
            return part
        }.joined(separator: " ")
    }
}

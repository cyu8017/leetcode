// LeetCode 1352 - Product of the Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers {
    private var p = [1]

    init() {}

    func add(_ num: Int) {
        if num == 0 { p = [1] }
        else { p.append(p.last! * num) }
    }

    func getProduct(_ k: Int) -> Int {
        if k >= p.count { return 0 }
        return p[p.count - 1] / p[p.count - 1 - k]
    }
}

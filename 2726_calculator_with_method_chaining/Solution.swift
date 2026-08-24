// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

import Foundation

class Calculator {
    private var val: Double

    init(_ val: Double) {
        self.val = val
    }

    func add(_ v: Double) -> Calculator {
        val += v
        return self
    }

    func subtract(_ v: Double) -> Calculator {
        val -= v
        return self
    }

    func multiply(_ v: Double) -> Calculator {
        val *= v
        return self
    }

    func divide(_ v: Double) -> Calculator {
        if v != 0 { val /= v }
        return self
    }

    func power(_ v: Double) -> Calculator {
        val = pow(val, v)
        return self
    }

    func getResult() -> Double {
        val
    }
}

class Solution {
    func calculatorCreate(_ val: Double) -> Calculator {
        Calculator(val)
    }
}

// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

var uniform: (Double, Double) -> Double = { _, _ in 0 }

func set_uniform(_ uniformFn: @escaping (Double, Double) -> Double) {
    uniform = uniformFn
}

class Solution {
    private var prefix: [Int]
    private var total: Int

    init(_ w: [Int]) {
        var runningTotal = 0
        var values: [Int] = []
        for weight in w {
            runningTotal += weight
            values.append(runningTotal)
        }
        prefix = values
        total = runningTotal
    }

    func pickIndex() -> Int {
        var target = Int(uniform(0, Double(total)))
        if target >= total {
            target = total - 1
        }
        var low = 0
        var high = prefix.count - 1
        while low < high {
            let mid = (low + high) / 2
            if prefix[mid] <= target {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return low
    }
}

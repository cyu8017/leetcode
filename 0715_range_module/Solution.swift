// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

class RangeModule {
    private var ranges = [(Int, Int)]()

    init() {}

    func addRange(_ left: Int, _ right: Int) {
        var left = left, right = right
        var nxt = [(Int, Int)]()
        var placed = false
        for (a, b) in ranges {
            if b < left {
                nxt.append((a, b))
            } else if a > right {
                if !placed { nxt.append((left, right)); placed = true }
                nxt.append((a, b))
            } else {
                left = min(left, a)
                right = max(right, b)
            }
        }
        if !placed { nxt.append((left, right)) }
        ranges = nxt
    }

    func queryRange(_ left: Int, _ right: Int) -> Bool {
        var lo = 0, hi = ranges.count - 1
        while lo <= hi {
            let mid = (lo + hi) / 2
            let (a, b) = ranges[mid]
            if b <= left { lo = mid + 1 }
            else if a >= right { hi = mid - 1 }
            else { return a <= left && b >= right }
        }
        return false
    }

    func removeRange(_ left: Int, _ right: Int) {
        var nxt = [(Int, Int)]()
        for (a, b) in ranges {
            if b <= left || a >= right {
                nxt.append((a, b))
            } else {
                if a < left { nxt.append((a, left)) }
                if b > right { nxt.append((right, b)) }
            }
        }
        ranges = nxt
    }
}

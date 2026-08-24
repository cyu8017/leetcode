// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

private class SegNode {
    var left: SegNode?
    var right: SegNode?
    var covered = false
}

class CountIntervals {
    private var root: SegNode?
    private var cnt = 0

    init() {}

    func add(_ left: Int, _ right: Int) {
        cnt += addRange(1, 1_000_000_000, left, right, &root)
    }

    func count() -> Int { cnt }

    @discardableResult
    private func addRange(_ L: Int, _ R: Int, _ l: Int, _ r: Int, _ node: inout SegNode?) -> Int {
        if node == nil { node = SegNode() }
        if node!.covered { return 0 }
        if l <= L && R <= r {
            node!.covered = true
            node!.left = nil
            node!.right = nil
            return R - L + 1
        }
        let mid = (L + R) / 2
        var added = 0
        if l <= mid {
            var leftChild = node!.left
            added += addRange(L, mid, l, r, &leftChild)
            node!.left = leftChild
        }
        if r > mid {
            var rightChild = node!.right
            added += addRange(mid + 1, R, l, r, &rightChild)
            node!.right = rightChild
        }
        if let left = node!.left, let right = node!.right, left.covered && right.covered {
            node!.covered = true
            node!.left = nil
            node!.right = nil
        }
        return added
    }
}

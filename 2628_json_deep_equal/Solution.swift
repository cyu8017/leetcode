// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

class Solution {
    func areDeeplyEqual(_ o1: Any?, _ o2: Any?) -> Bool {
        switch (o1, o2) {
        case (nil, nil):
            return true
        case (let a as Int, let b as Int):
            return a == b
        case (let a as Double, let b as Double):
            return a == b
        case (let a as Bool, let b as Bool):
            return a == b
        case (let a as String, let b as String):
            return a == b
        case (let a as [Any?], let b as [Any?]):
            guard a.count == b.count else { return false }
            for i in 0..<a.count where !areDeeplyEqual(a[i], b[i]) { return false }
            return true
        case (let a as [String: Any?], let b as [String: Any?]):
            guard a.count == b.count else { return false }
            for (k, v) in a where !areDeeplyEqual(v, b[k] ?? nil) { return false }
            return true
        default:
            return false
        }
    }

    func areDeeplyEqual(_ o1: String, _ o2: String) -> Bool {
        o1 == o2
    }
}

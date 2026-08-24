// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Expect {
    private let val: Int

    init(_ val: Int) {
        self.val = val
    }

    func toBe(_ other: Int) -> Bool {
        if val == other { return true }
        fatalError("Not Equal")
    }

    func notToBe(_ other: Int) -> Bool {
        if val != other { return true }
        fatalError("Equal")
    }
}

class Solution {
    func expect(_ val: Int) -> Expect {
        Expect(val)
    }
}

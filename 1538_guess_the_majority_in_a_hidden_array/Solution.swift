// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

class ArrayReader {
    private let nums: [Int]
    init(_ nums: [Int]) { self.nums = nums }
    func query(_ a: Int, _ b: Int, _ c: Int, _ d: Int) -> Int {
        let ones = nums[a] + nums[b] + nums[c] + nums[d]
        if ones == 0 || ones == 4 { return 4 }
        if ones == 1 || ones == 3 { return 2 }
        return 0
    }
    func length() -> Int { nums.count }
}

class Solution {
    func guessMajority(_ nums: [Int]) -> Int {
        guessMajority(ArrayReader(nums))
    }

    func guessMajority(_ reader: ArrayReader) -> Int {
        let n = reader.length()
        let firstFour = reader.query(0, 1, 2, 3)
        let shifted = reader.query(1, 2, 3, 4)
        var same = 1, different = 0, differentIndex = -1, laterDifferent = -1
        let fourSame = firstFour == shifted
        if fourSame { same += 1 } else { different += 1; differentIndex = 4 }
        let checks = [[0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4]]
        for (index, args) in checks.enumerated() {
            if reader.query(args[0], args[1], args[2], args[3]) == shifted {
                same += 1
            } else {
                different += 1
                differentIndex = index + 1
            }
        }
        if n > 5 {
            for i in 5..<n {
                let iSameAsFour = reader.query(1, 2, 3, i) == shifted
                if iSameAsFour == fourSame {
                    same += 1
                } else {
                    different += 1
                    differentIndex = i
                    if laterDifferent == -1 { laterDifferent = i }
                }
            }
        }
        if same == different { return -1 }
        return same > different ? 0 : (laterDifferent != -1 ? laterDifferent : differentIndex)
    }
}

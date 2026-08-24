// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

class Solution {
    private class BIT {
        var n: Int
        var c: [Int]
        init(_ n_: Int) {
            n = n_
            c = [Int](repeating: 0, count: n_ + 1)
        }
        func update(_ x: Int, _ delta: Int) {
            var x = x
            while x <= n {
                c[x] += delta
                x += x & -x
            }
        }
        func query(_ x: Int) -> Int {
            var x = x, s = 0
            while x > 0 {
                s += c[x]
                x -= x & -x
            }
            return s
        }
    }

    func countMajoritySubarrays(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        let tree = BIT(2 * n + 1)
        var s = n + 1
        tree.update(s, 1)
        var ans = 0
        for x in nums {
            if x == target { s += 1 } else { s -= 1 }
            ans += tree.query(s - 1)
            tree.update(s, 1)
        }
        return ans
    }
}

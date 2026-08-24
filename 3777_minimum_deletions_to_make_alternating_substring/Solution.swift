// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

class Solution {
    private class BIT {
        var n: Int
        var c: [Int]
        init(_ n_: Int) { n = n_; c = [Int](repeating: 0, count: n_ + 1) }
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

    func minDeletions(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var nums = [Int](repeating: 0, count: n)
        let bit = BIT(n)
        if n > 1 {
            for i in 1..<n {
                if chars[i] == chars[i - 1] {
                    nums[i] = 1
                    bit.update(i + 1, 1)
                }
            }
        }
        var ans = [Int]()
        for q in queries {
            if q[0] == 1 {
                let j = q[1]
                var delta = (nums[j] ^ 1) - nums[j]
                nums[j] ^= 1
                bit.update(j + 1, delta)
                if j + 1 < n {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1]
                    nums[j + 1] ^= 1
                    bit.update(j + 2, delta)
                }
            } else {
                let l = q[1], r = q[2]
                ans.append(bit.query(r + 1) - bit.query(l + 1))
            }
        }
        return ans
    }
}

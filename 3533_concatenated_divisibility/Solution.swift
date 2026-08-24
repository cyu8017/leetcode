// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

class Solution {
    var n = 0, k = 0
    var nums = [Int]()
    var pows = [Int]()
    var memo = [Int: Bool]()

    func concatenatedDivisibility(_ nums0: [Int], _ k0: Int) -> [Int] {
        nums = nums0.sorted()
        k = k0
        n = nums.count
        pows = Array(repeating: 0, count: n)
        for i in 0..<n {
            var p = 1
            let num = nums[i]
            if num == 0 { p = 10 % k }
            else {
                var x = num
                while x > 0 { p = p * 10 % k; x /= 10 }
            }
            pows[i] = p
        }
        memo = [:]
        if !dp(0, 0) { return [] }
        return reconstruct(0, 0)
    }

    func dp(_ mask: Int, _ mod: Int) -> Bool {
        if mask == (1 << n) - 1 { return mod == 0 }
        let key = (mask << 32) | mod
        if let v = memo[key] { return v }
        for i in 0..<n {
            if ((mask >> i) & 1) == 0 {
                let nm = (mod * pows[i] + nums[i]) % k
                if dp(mask | (1 << i), nm) {
                    memo[key] = true
                    return true
                }
            }
        }
        memo[key] = false
        return false
    }

    func reconstruct(_ mask: Int, _ mod: Int) -> [Int] {
        for i in 0..<n {
            if ((mask >> i) & 1) == 0 {
                let nm = (mod * pows[i] + nums[i]) % k
                if dp(mask | (1 << i), nm) {
                    var rest = reconstruct(mask | (1 << i), nm)
                    rest.insert(nums[i], at: 0)
                    return rest
                }
            }
        }
        return []
    }
}

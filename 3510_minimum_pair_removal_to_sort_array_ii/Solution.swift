// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

class Solution {
    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var nums = nums
        let n = nums.count
        var inv = 0, ans = 0
        var sl = [(Int, Int)]()
        var alive = Array(repeating: true, count: n)
        var nxt = Array(0..<n)
        var prv = Array(0..<n)
        for i in 0..<n {
            nxt[i] = i + 1 < n ? i + 1 : -1
            prv[i] = i - 1 >= 0 ? i - 1 : -1
        }
        func slInsert(_ sum: Int, _ i: Int) {
            var lo = 0, hi = sl.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sl[mid].0 < sum || (sl[mid].0 == sum && sl[mid].1 < i) { lo = mid + 1 }
                else { hi = mid }
            }
            sl.insert((sum, i), at: lo)
        }
        func slRemove(_ sum: Int, _ i: Int) {
            var lo = 0, hi = sl.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sl[mid].0 < sum || (sl[mid].0 == sum && sl[mid].1 < i) { lo = mid + 1 }
                else { hi = mid }
            }
            if lo < sl.count && sl[lo].0 == sum && sl[lo].1 == i { sl.remove(at: lo) }
        }
        for i in 0..<(n - 1) {
            if nums[i] > nums[i + 1] { inv += 1 }
            slInsert(nums[i] + nums[i + 1], i)
        }
        while inv > 0 {
            ans += 1
            var p: (Int, Int)? = nil
            while !sl.isEmpty {
                let cand = sl.removeFirst()
                let i = cand.1
                if !alive[i] { continue }
                let j = nxt[i]
                if j < 0 || !alive[j] { continue }
                if cand.0 != nums[i] + nums[j] { continue }
                p = cand
                break
            }
            guard let p = p else { break }
            let s = p.0, i = p.1
            let j = nxt[i]
            if nums[i] > nums[j] { inv -= 1 }
            let h = prv[i]
            if h >= 0 {
                if nums[h] > nums[i] { inv -= 1 }
                slRemove(nums[h] + nums[i], h)
                if nums[h] > s { inv += 1 }
                slInsert(nums[h] + s, h)
            }
            let k = nxt[j]
            if k >= 0 {
                if nums[j] > nums[k] { inv -= 1 }
                slRemove(nums[j] + nums[k], j)
                if s > nums[k] { inv += 1 }
                slInsert(s + nums[k], i)
            }
            nums[i] = s
            alive[j] = false
            nxt[i] = k
            if k >= 0 { prv[k] = i }
        }
        return ans
    }
}

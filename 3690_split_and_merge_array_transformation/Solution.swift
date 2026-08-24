// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

class Solution {
    func minSplitMerge(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        func key(_ a: [Int]) -> String { a.map(String.init).joined(separator: ",") }
        var vis = Set<String>()
        vis.insert(key(nums1))
        var q = [nums1]
        var ans = 0
        while true {
            var nq = [[Int]]()
            for cur in q {
                if cur == nums2 { return ans }
                for l in 0..<n {
                    for r in l..<n {
                        var remain = [Int]()
                        var sub = [Int]()
                        for i in 0..<l { remain.append(cur[i]) }
                        if r + 1 < n {
                            for i in (r + 1)..<n { remain.append(cur[i]) }
                        }
                        for i in l...r { sub.append(cur[i]) }
                        for pos in 0...remain.count {
                            var nxt = Array(remain[0..<pos]) + sub + Array(remain[pos...])
                            let k = key(nxt)
                            if !vis.contains(k) {
                                vis.insert(k)
                                nq.append(nxt)
                            }
                        }
                    }
                }
            }
            q = nq
            ans += 1
        }
    }
}

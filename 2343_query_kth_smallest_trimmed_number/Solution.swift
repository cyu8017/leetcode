// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

class Solution {
    func smallestTrimmedNumbers(_ nums: [String], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        return queries.map { q in
            let k = q[0], trim = q[1]
            var arr: [(String, Int)] = []
            for i in 0..<n {
                let s = nums[i]
                arr.append((String(s.suffix(trim)), i))
            }
            arr.sort {
                if $0.0 != $1.0 { return $0.0 < $1.0 }
                return $0.1 < $1.1
            }
            return arr[k - 1].1
        }
    }
}

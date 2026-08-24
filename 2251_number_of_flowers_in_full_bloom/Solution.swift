// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution {
    func fullBloomFlowers(_ flowers: [[Int]], _ people: [Int]) -> [Int] {
        let start = flowers.map { $0[0] }.sorted()
        let end = flowers.map { $0[1] }.sorted()
        func upperBound(_ a: [Int], _ t: Int) -> Int {
            var lo = 0, hi = a.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if a[mid] <= t { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
        func lowerBound(_ a: [Int], _ t: Int) -> Int {
            var lo = 0, hi = a.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if a[mid] < t { lo = mid + 1 } else { hi = mid }
            }
            return lo
        }
        return people.map { t in upperBound(start, t) - lowerBound(end, t) }
    }
}

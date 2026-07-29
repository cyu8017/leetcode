// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution {
    func sampleStats(_ count: [Int]) -> [Double] {
        let total = count.reduce(0, +)
        var minimum = 0
        for i in 0..<256 {
            if count[i] > 0 {
                minimum = i
                break
            }
        }
        var maximum = 0
        for i in stride(from: 255, through: 0, by: -1) {
            if count[i] > 0 {
                maximum = i
                break
            }
        }
        var meanSum = 0.0
        for i in 0..<256 {
            meanSum += Double(i * count[i])
        }
        let mean = meanSum / Double(total)
        var mode = 0
        for i in 0..<256 {
            if count[i] > count[mode] {
                mode = i
            }
        }
        let mid1 = (total + 1) / 2
        let mid2 = (total + 2) / 2
        var seen = 0
        var first: Int?
        var second: Int?
        for i in 0..<256 {
            seen += count[i]
            if first == nil && seen >= mid1 {
                first = i
            }
            if second == nil && seen >= mid2 {
                second = i
                break
            }
        }
        let median = Double(first! + second!) / 2.0
        return [Double(minimum), Double(maximum), mean, median, Double(mode)]
    }
}

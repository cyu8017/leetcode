// LeetCode 1776 - Car Fleet II
// https://leetcode.com/problems/car-fleet-ii/

class Solution {
    func getCollisionTimes(_ cars: [[Int]]) -> [Double] {
        let n = cars.count
        var ans = [Double](repeating: -1.0, count: n)
        var stack = [Int]()
        for i in stride(from: n - 1, through: 0, by: -1) {
            let pos = cars[i][0]
            let speed = cars[i][1]
            while let j = stack.last {
                if speed <= cars[j][1] {
                    stack.removeLast()
                    continue
                }
                let t = Double(cars[j][0] - pos) / Double(speed - cars[j][1])
                if ans[j] < 0 || t <= ans[j] {
                    ans[i] = t
                    break
                }
                stack.removeLast()
            }
            stack.append(i)
        }
        return ans
    }
}

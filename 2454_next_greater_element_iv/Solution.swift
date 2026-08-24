// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

class Solution {
    func secondGreaterElement(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = [Int](repeating: -1, count: n)
        var stack1 = [Int]()
        var stack2 = [Int]()
        for i in 0..<n {
            let x = nums[i]
            while !stack2.isEmpty && nums[stack2.last!] < x {
                ans[stack2.removeLast()] = x
            }
            var tmp = [Int]()
            while !stack1.isEmpty && nums[stack1.last!] < x {
                tmp.append(stack1.removeLast())
            }
            for j in stride(from: tmp.count - 1, through: 0, by: -1) {
                stack2.append(tmp[j])
            }
            stack1.append(i)
        }
        return ans
    }
}

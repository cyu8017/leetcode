// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

class Solution {
    func maximizeXor(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let nums = nums.sorted()
        let order = queries.indices.sorted { queries[$0][1] < queries[$1][1] }

        var children: [[Int]] = [[-1, -1]]

        func insert(_ num: Int) {
            var node = 0
            for bit in stride(from: 31, through: 0, by: -1) {
                let b = (num >> bit) & 1
                if children[node][b] == -1 {
                    children[node][b] = children.count
                    children.append([-1, -1])
                }
                node = children[node][b]
            }
        }

        var ans = [Int](repeating: -1, count: queries.count)
        var added = 0
        for qi in order {
            let x = queries[qi][0]
            let limit = queries[qi][1]
            while added < nums.count && nums[added] <= limit {
                insert(nums[added])
                added += 1
            }
            if added == 0 {
                continue
            }
            var node = 0
            var value = 0
            for bit in stride(from: 31, through: 0, by: -1) {
                let b = (x >> bit) & 1
                let want = b ^ 1
                if children[node][want] != -1 {
                    value |= 1 << bit
                    node = children[node][want]
                } else {
                    node = children[node][b]
                }
            }
            ans[qi] = value
        }
        return ans
    }
}

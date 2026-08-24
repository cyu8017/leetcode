// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

class Solution {
    func oddEvenJumps(_ arr: [Int]) -> Int {
        let n = arr.count
        var nextHigher = Array(repeating: 0, count: n)
        var nextLower = Array(repeating: 0, count: n)
        var order = Array(0..<n)
        order.sort { arr[$0] == arr[$1] ? $0 < $1 : arr[$0] < arr[$1] }
        var stack = [Int]()
        for i in order {
            while !stack.isEmpty && stack.last! < i {
                nextHigher[stack.removeLast()] = i
            }
            stack.append(i)
        }
        stack.removeAll()
        order.sort { arr[$0] == arr[$1] ? $0 < $1 : arr[$0] > arr[$1] }
        for i in order {
            while !stack.isEmpty && stack.last! < i {
                nextLower[stack.removeLast()] = i
            }
            stack.append(i)
        }
        var odd = Array(repeating: false, count: n)
        var even = Array(repeating: false, count: n)
        odd[n - 1] = true
        even[n - 1] = true
        for i in stride(from: n - 2, through: 0, by: -1) {
            if nextHigher[i] != 0 { odd[i] = even[nextHigher[i]] }
            if nextLower[i] != 0 { even[i] = odd[nextLower[i]] }
        }
        return odd.filter { $0 }.count
    }
}

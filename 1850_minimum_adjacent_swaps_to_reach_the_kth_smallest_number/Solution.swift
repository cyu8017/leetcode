// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution {
    func getMinSwaps(_ num: String, _ k: Int) -> Int {
        var target = Array(num)
        for _ in 0..<k {
            nextPermutation(&target)
        }
        var source = Array(num)
        var swaps = 0
        for i in 0..<source.count {
            if source[i] == target[i] { continue }
            var j = i
            while source[j] != target[i] { j += 1 }
            while j > i {
                source.swapAt(j, j - 1)
                swaps += 1
                j -= 1
            }
        }
        return swaps
    }

    private func nextPermutation(_ arr: inout [Character]) {
        var i = arr.count - 2
        while i >= 0 && arr[i] >= arr[i + 1] { i -= 1 }
        if i < 0 {
            arr.reverse()
            return
        }
        var j = arr.count - 1
        while arr[j] <= arr[i] { j -= 1 }
        arr.swapAt(i, j)
        arr[(i + 1)...].reverse()
    }
}

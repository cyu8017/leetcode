// LeetCode 3049 - Earliest Second to Mark Indices II
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

private struct MinHeap {
    private var data: [Int] = []
    var count: Int { data.count }
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ x: Int) {
        data.append(x)
        siftUp(data.count - 1)
    }
    mutating func pop() -> Int {
        let top = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            siftDown(0)
        }
        return top
    }
    private mutating func siftUp(_ i: Int) {
        var idx = i
        while idx > 0 {
            let p = (idx - 1) / 2
            if data[p] <= data[idx] { break }
            data.swapAt(p, idx)
            idx = p
        }
    }
    private mutating func siftDown(_ i: Int) {
        var idx = i
        while true {
            var smallest = idx
            let l = idx * 2 + 1, r = idx * 2 + 2
            if l < data.count && data[l] < data[smallest] { smallest = l }
            if r < data.count && data[r] < data[smallest] { smallest = r }
            if smallest == idx { break }
            data.swapAt(smallest, idx)
            idx = smallest
        }
    }
}

class Solution {
    func earliestSecondToMarkIndices(_ nums: [Int], _ changeIndices: [Int]) -> Int {
        let secondToIndex = getSecondToIndex(nums, changeIndices)
        var numsSum = 0
        for v in nums { numsSum += v }
        var l = 0, r = changeIndices.count + 1
        while l < r {
            let m = (l + r) / 2
            if canMark(nums, secondToIndex, m, numsSum) {
                r = m
            } else {
                l = m + 1
            }
        }
        return l <= changeIndices.count ? l : -1
    }

    private func getSecondToIndex(_ nums: [Int], _ changeIndices: [Int]) -> [Int: Int] {
        var indexToFirstSecond: [Int: Int] = [:]
        for second in 0..<changeIndices.count {
            let index = changeIndices[second] - 1
            if nums[index] > 0 && indexToFirstSecond[index] == nil {
                indexToFirstSecond[index] = second
            }
        }
        var secondToIndex: [Int: Int] = [:]
        for (index, second) in indexToFirstSecond {
            secondToIndex[second] = index
        }
        return secondToIndex
    }

    private func canMark(_ nums: [Int], _ secondToIndex: [Int: Int], _ maxSecond: Int, _ numsSum: Int) -> Bool {
        var h = MinHeap()
        var marks = 0
        if maxSecond <= 0 { return numsSum + nums.count <= 0 }
        for second in stride(from: maxSecond - 1, through: 0, by: -1) {
            if let idx = secondToIndex[second] {
                h.push(nums[idx])
                if marks == 0 {
                    _ = h.pop()
                    marks += 1
                } else {
                    marks -= 1
                }
            } else {
                marks += 1
            }
        }
        var heapSum = 0
        var heapSize = 0
        var heap = h
        while !heap.isEmpty {
            heapSum += heap.pop()
            heapSize += 1
        }
        let decrementAndMarkCost = numsSum - heapSum + (nums.count - heapSize)
        let zeroAndMarkCost = heapSize + heapSize
        return decrementAndMarkCost + zeroAndMarkCost <= maxSecond
    }
}

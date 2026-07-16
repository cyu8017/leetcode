// LeetCode 0358 - Rearrange String k Distance Apart
// https://leetcode.com/problems/rearrange-string-k-distance-apart/

class Solution {
    func rearrangeString(_ s: String, _ k: Int) -> String {
        var counts: [Character: Int] = [:]
        for char in s {
            counts[char, default: 0] += 1
        }

        let maxFreq = counts.values.max() ?? 0
        let maxFreqChars = counts.values.filter { $0 == maxFreq }.count
        if (s.count - maxFreqChars) < (maxFreq - 1) * (k - 1) {
            return ""
        }

        var heap: [(Int, Character)] = counts.map { (-$0.value, $0.key) }

        func heapPush(_ item: (Int, Character)) {
            heap.append(item)
            var index = heap.count - 1
            while index > 0 {
                let parent = (index - 1) / 2
                if heap[parent] <= heap[index] {
                    break
                }
                heap.swapAt(parent, index)
                index = parent
            }
        }

        func heapPop() -> (Int, Character) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var index = 0
                while true {
                    var smallest = index
                    let left = 2 * index + 1
                    let right = left + 1
                    if left < heap.count && heap[left] < heap[smallest] {
                        smallest = left
                    }
                    if right < heap.count && heap[right] < heap[smallest] {
                        smallest = right
                    }
                    if smallest == index {
                        break
                    }
                    heap.swapAt(index, smallest)
                    index = smallest
                }
            }
            return top
        }

        heapify(&heap)

        var queue: [(Int, Character, Int)] = []
        var result = ""
        var index = 0

        while !heap.isEmpty || !queue.isEmpty {
            while !queue.isEmpty && queue[0].2 <= index {
                let entry = queue.removeFirst()
                heapPush((entry.0, entry.1))
            }

            if heap.isEmpty {
                return ""
            }

            let entry = heapPop()
            let count = entry.0
            let char = entry.1
            result.append(char)
            if count + 1 < 0 {
                queue.append((count + 1, char, index + k))
            }
            index += 1
        }

        return result
    }

    private func heapify(_ heap: inout [(Int, Character)]) {
        for start in stride(from: heap.count / 2 - 1, through: 0, by: -1) {
            var index = start
            while true {
                var smallest = index
                let left = 2 * index + 1
                let right = left + 1
                if left < heap.count && heap[left] < heap[smallest] {
                    smallest = left
                }
                if right < heap.count && heap[right] < heap[smallest] {
                    smallest = right
                }
                if smallest == index {
                    break
                }
                heap.swapAt(index, smallest)
                index = smallest
            }
        }
    }
}

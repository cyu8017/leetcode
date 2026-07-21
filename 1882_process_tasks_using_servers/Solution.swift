// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

class Solution {
    func assignTasks(_ servers: [Int], _ tasks: [Int]) -> [Int] {
        var available: [(Int, Int)] = servers.enumerated().map { ($1, $0) }
        var busy: [(Int, Int, Int)] = []
        var answer: [Int] = []
        var time = 0

        heapifyAvailable(&available)

        for (moment, task) in tasks.enumerated() {
            time = max(time, moment)
            while !busy.isEmpty && busy[0].0 <= time {
                let (_, weight, index) = heapPopBusy(&busy)
                heapPushAvailable(&available, (weight, index))
            }

            while available.isEmpty {
                time = busy[0].0
                while !busy.isEmpty && busy[0].0 <= time {
                    let (_, weight, index) = heapPopBusy(&busy)
                    heapPushAvailable(&available, (weight, index))
                }
            }

            let (weight, index) = heapPopAvailable(&available)
            heapPushBusy(&busy, (time + task, weight, index))
            answer.append(index)
        }

        return answer
    }

    private func heapifyAvailable(_ heap: inout [(Int, Int)]) {
        if heap.isEmpty {
            return
        }
        for i in stride(from: heap.count / 2 - 1, through: 0, by: -1) {
            siftDownAvailable(&heap, i)
        }
    }

    private func heapPushAvailable(_ heap: inout [(Int, Int)], _ item: (Int, Int)) {
        heap.append(item)
        var index = heap.count - 1
        while index > 0 {
            let parent = (index - 1) / 2
            if !lessAvailable(heap[index], heap[parent]) {
                break
            }
            heap.swapAt(parent, index)
            index = parent
        }
    }

    private func heapPopAvailable(_ heap: inout [(Int, Int)]) -> (Int, Int) {
        let top = heap[0]
        let last = heap.removeLast()
        if heap.isEmpty {
            return top
        }
        heap[0] = last
        siftDownAvailable(&heap, 0)
        return top
    }

    private func siftDownAvailable(_ heap: inout [(Int, Int)], _ start: Int) {
        var index = start
        while true {
            var smallest = index
            let left = index * 2 + 1
            let right = index * 2 + 2
            if left < heap.count && lessAvailable(heap[left], heap[smallest]) {
                smallest = left
            }
            if right < heap.count && lessAvailable(heap[right], heap[smallest]) {
                smallest = right
            }
            if smallest == index {
                break
            }
            heap.swapAt(index, smallest)
            index = smallest
        }
    }

    private func lessAvailable(_ lhs: (Int, Int), _ rhs: (Int, Int)) -> Bool {
        if lhs.0 != rhs.0 {
            return lhs.0 < rhs.0
        }
        return lhs.1 < rhs.1
    }

    private func heapPushBusy(_ heap: inout [(Int, Int, Int)], _ item: (Int, Int, Int)) {
        heap.append(item)
        var index = heap.count - 1
        while index > 0 {
            let parent = (index - 1) / 2
            if !lessBusy(heap[index], heap[parent]) {
                break
            }
            heap.swapAt(parent, index)
            index = parent
        }
    }

    private func heapPopBusy(_ heap: inout [(Int, Int, Int)]) -> (Int, Int, Int) {
        let top = heap[0]
        let last = heap.removeLast()
        if heap.isEmpty {
            return top
        }
        heap[0] = last
        siftDownBusy(&heap, 0)
        return top
    }

    private func siftDownBusy(_ heap: inout [(Int, Int, Int)], _ start: Int) {
        var index = start
        while true {
            var smallest = index
            let left = index * 2 + 1
            let right = index * 2 + 2
            if left < heap.count && lessBusy(heap[left], heap[smallest]) {
                smallest = left
            }
            if right < heap.count && lessBusy(heap[right], heap[smallest]) {
                smallest = right
            }
            if smallest == index {
                break
            }
            heap.swapAt(index, smallest)
            index = smallest
        }
    }

    private func lessBusy(_ lhs: (Int, Int, Int), _ rhs: (Int, Int, Int)) -> Bool {
        if lhs.0 != rhs.0 {
            return lhs.0 < rhs.0
        }
        if lhs.1 != rhs.1 {
            return lhs.1 < rhs.1
        }
        return lhs.2 < rhs.2
    }
}

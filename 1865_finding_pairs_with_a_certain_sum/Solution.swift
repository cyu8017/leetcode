// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs {
    private var nums1: [Int]
    private var nums2: [Int]
    private var counts: [Int: Int] = [:]

    init(_ nums1: [Int], _ nums2: [Int]) {
        self.nums1 = nums1
        self.nums2 = nums2
        for num in nums2 {
            counts[num, default: 0] += 1
        }
    }

    func add(_ index: Int, _ val: Int) {
        counts[nums2[index], default: 0] -= 1
        nums2[index] += val
        counts[nums2[index], default: 0] += 1
    }

    func count(_ tot: Int) -> Int {
        var result = 0
        for num in nums1 {
            result += counts[tot - num, default: 0]
        }
        return result
    }
}

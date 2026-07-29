// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

class MountainArray {
    func get(_ index: Int) -> Int { 0 }
    func length() -> Int { 0 }
}

class Solution {
    func findInMountainArray(_ target: Int, _ mountainArr: MountainArray) -> Int {
        let n = mountainArr.length()
        var lo = 0
        var hi = n - 1
        while lo < hi {
            let mid = (lo + hi) / 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        let peak = lo
        lo = 0
        hi = peak
        while lo <= hi {
            let mid = (lo + hi) / 2
            let val = mountainArr.get(mid)
            if val == target {
                return mid
            }
            if val < target {
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        lo = peak + 1
        hi = n - 1
        while lo <= hi {
            let mid = (lo + hi) / 2
            let val = mountainArr.get(mid)
            if val == target {
                return mid
            }
            if val > target {
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return -1
    }
}

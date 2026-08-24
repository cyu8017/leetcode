// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

protocol Street {
    func closeDoor()
    func isDoorOpen() -> Bool
    func moveRight()
}

class Solution {
    func houseCount(_ street: Street, _ k: Int) -> Int {
        for _ in 0..<k { street.moveRight() }
        var ans = 0
        for _ in 0..<k {
            if street.isDoorOpen() {
                ans += 1
                street.closeDoor()
            }
            street.moveRight()
        }
        return ans
    }

    func houseCount(_ street: [Int], _ k: Int) -> Int {
        let n = street.count
        if n == 0 { return 0 }
        guard let start = street.firstIndex(of: 1) else { return 0 }
        var count = 1, moves = 0, i2 = start
        while moves < k {
            i2 = (i2 + 1) % n
            moves += 1
            if i2 == start { break }
            if street[i2] == 1 { count += 1 }
        }
        return count
    }
}

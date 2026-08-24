// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/

protocol Street {
    func openDoor()
    func closeDoor()
    func isDoorOpen() -> Bool
    func moveRight()
    func moveLeft()
}

class Solution {
    func countHouses(_ street: Street, _ k: Int) -> Int {
        for _ in 0..<k {
            street.closeDoor()
            street.moveRight()
        }
        var ans = 0
        while true {
            ans += 1
            street.openDoor()
            street.moveRight()
            if street.isDoorOpen() { break }
        }
        return ans
    }
}

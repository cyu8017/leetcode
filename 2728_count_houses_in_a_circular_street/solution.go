// LeetCode 2728 - Count Houses in a Circular Street
// https://leetcode.com/problems/count-houses-in-a-circular-street/


type Street interface {
	OpenDoor()
	CloseDoor()
	IsDoorOpen() bool
	MoveRight()
	MoveLeft()
}

func countHouses(street Street, k int) int {
	for i := 0; i < k; i++ {
		street.CloseDoor()
		street.MoveRight()
	}
	ans := 0
	for {
		ans++
		street.OpenDoor()
		street.MoveRight()
		if street.IsDoorOpen() {
			break
		}
	}
	return ans
}

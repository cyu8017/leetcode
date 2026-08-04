// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

type ArrayReader struct {
	nums []int
}

func (this *ArrayReader) query(a, b, c, d int) int {
	ones := this.nums[a] + this.nums[b] + this.nums[c] + this.nums[d]
	if ones == 0 || ones == 4 {
		return 4
	}
	if ones == 1 || ones == 3 {
		return 2
	}
	return 0
}

func (this *ArrayReader) length() int {
	return len(this.nums)
}

func guessMajority(nums []int) int {
	reader := &ArrayReader{nums: nums}
	n := reader.length()
	firstFour := reader.query(0, 1, 2, 3)
	shifted := reader.query(1, 2, 3, 4)
	same, different, differentIndex, laterDifferent := 1, 0, -1, -1
	fourSame := firstFour == shifted
	if fourSame {
		same++
	} else {
		different++
		differentIndex = 4
	}
	checks := [][4]int{{0, 2, 3, 4}, {0, 1, 3, 4}, {0, 1, 2, 4}}
	for index, args := range checks {
		if reader.query(args[0], args[1], args[2], args[3]) == shifted {
			same++
		} else {
			different++
			differentIndex = index + 1
		}
	}
	for i := 5; i < n; i++ {
		iSameAsFour := reader.query(1, 2, 3, i) == shifted
		if iSameAsFour == fourSame {
			same++
		} else {
			different++
			differentIndex = i
			if laterDifferent == -1 {
				laterDifferent = i
			}
		}
	}
	if same == different {
		return -1
	}
	if same > different {
		return 0
	}
	if laterDifferent != -1 {
		return laterDifferent
	}
	return differentIndex
}

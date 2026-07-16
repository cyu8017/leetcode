// LeetCode 0379 - Design Phone Directory
// https://leetcode.com/problems/design-phone-directory/

type PhoneDirectory struct {
	available []bool
}

func Constructor(maxNumbers int) PhoneDirectory {
	available := make([]bool, maxNumbers)
	for number := 0; number < maxNumbers; number++ {
		available[number] = true
	}
	return PhoneDirectory{available: available}
}

func (this *PhoneDirectory) Get() int {
	for number, isAvailable := range this.available {
		if isAvailable {
			this.available[number] = false
			return number
		}
	}
	return -1
}

func (this *PhoneDirectory) Check(number int) bool {
	if number < 0 || number >= len(this.available) {
		return false
	}
	return this.available[number]
}

func (this *PhoneDirectory) Release(number int) {
	if number >= 0 && number < len(this.available) {
		this.available[number] = true
	}
}

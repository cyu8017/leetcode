// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/


type Expect struct{ val interface{} }

func expect(val interface{}) Expect {
	return Expect{val: val}
}

func (e Expect) ToBe(other interface{}) bool {
	if e.val != other {
		panic("Not Equal")
	}
	return true
}

func (e Expect) NotToBe(other interface{}) bool {
	if e.val == other {
		panic("Equal")
	}
	return true
}

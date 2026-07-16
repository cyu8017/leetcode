// LeetCode 0170 - Two Sum III - Data structure design
type TwoSum struct { counts map[int]int }
func Constructor() TwoSum { return TwoSum{counts: make(map[int]int)} }
func (this *TwoSum) Add(number int) { this.counts[number]++ }
func (this *TwoSum) Find(value int) bool {
    for number, count := range this.counts {
        complement := value - number
        if complement == number {
            if count >= 2 { return true }
        } else if _, ok := this.counts[complement]; ok { return true }
    }
    return false
}
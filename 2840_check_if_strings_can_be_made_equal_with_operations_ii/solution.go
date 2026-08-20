// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

func checkStrings(s1 string, s2 string) bool {
	even1, odd1 := [26]int{}, [26]int{}
	even2, odd2 := [26]int{}, [26]int{}
	for i := 0; i < len(s1); i++ {
		if i%2 == 0 {
			even1[s1[i]-'a']++
			even2[s2[i]-'a']++
		} else {
			odd1[s1[i]-'a']++
			odd2[s2[i]-'a']++
		}
	}
	return even1 == even2 && odd1 == odd2
}

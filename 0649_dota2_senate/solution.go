// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

func predictPartyVictory(senate string) string {
	radiant := []int{}
	dire := []int{}
	n := len(senate)
	for i := 0; i < n; i++ {
		if senate[i] == 'R' {
			radiant = append(radiant, i)
		} else {
			dire = append(dire, i)
		}
	}
	for len(radiant) > 0 && len(dire) > 0 {
		r := radiant[0]
		d := dire[0]
		radiant = radiant[1:]
		dire = dire[1:]
		if r < d {
			radiant = append(radiant, r+n)
		} else {
			dire = append(dire, d+n)
		}
	}
	if len(radiant) > 0 {
		return "Radiant"
	}
	return "Dire"
}

// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

import "sort"

func minDamage(power int, damage []int, health []int) int64 {
	n := len(damage)
	type enemy struct{ dmg, hits int }
	arr := make([]enemy, n)
	totalDmg := 0
	for i := 0; i < n; i++ {
		hits := (health[i] + power - 1) / power
		arr[i] = enemy{damage[i], hits}
		totalDmg += damage[i]
	}
	sort.Slice(arr, func(i, j int) bool {
		// kill i before j if damage_i/hits_i better ordering: hits_i * dmg_j < hits_j * dmg_i
		return int64(arr[i].hits)*int64(arr[j].dmg) < int64(arr[j].hits)*int64(arr[i].dmg)
	})
	var ans int64
	cur := int64(totalDmg)
	for _, e := range arr {
		ans += cur * int64(e.hits)
		cur -= int64(e.dmg)
	}
	return ans
}

// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

func makeStringGood(s string) int {
	freq := [26]int{}
	for _, c := range s {
		freq[c-'a']++
	}
	ans := len(s)
	for target := 0; target <= len(s); target++ {
		ops := 0
		extra := 0
		for _, f := range freq {
			if f > target {
				extra += f - target
			} else {
				ops += target - f
			}
		}
		// extras can convert
		if extra >= ops {
			if extra < ans { // actually ops is conversions needed into deficient; extras provide
				ans = extra // wait
			}
		}
		use := ops
		if extra < ops {
			use = ops // need delete extras? 
		}
		// Correct: for each target frequency t
		cost := 0
		surplus := 0
		for _, f := range freq {
			if f >= target {
				surplus += f - target
			} else {
				need := target - f
				if surplus >= need {
					surplus -= need
					cost += need // convert
				} else {
					cost += surplus // convert all surplus
					need -= surplus
					surplus = 0
					cost += need // insert or from deletes elsewhere
				}
			}
		}
		cost += surplus // delete remaining surplus? for making all equal to target, yes delete
		// Actually better known approach:
		_ = cost
	}
	// Simpler O(26*n):
	ans = len(s)
	for t := 1; t <= len(s); t++ {
		dp0, dp1 := 0, 0 // min ops processing letters, with carry convert capability
		// process a..z
		change := 0
		for i := 0; i < 26; i++ {
			f := freq[i]
			if f > t {
				change += f - t
			} else {
				need := t - f
				if change >= need {
					change -= need
				} else {
					ans += 0
				}
			}
		}
		ops := 0
		pool := 0
		for i := 0; i < 26; i++ {
			f := freq[i]
			if f > t {
				pool += f - t
			}
		}
		for i := 0; i < 26; i++ {
			f := freq[i]
			if f < t {
				need := t - f
				use := need
				if use > pool {
					use = pool
				}
				ops += need // each need is one op (insert or convert)
				pool -= use
				// converts counted in ops; deletes of unused pool later
			}
		}
		ops += pool // delete leftover
		// overcount converts: convert is 1 op not 2
		// recalculate properly
		ops = 0
		pool = 0
		for i := 0; i < 26; i++ {
			if freq[i] > t {
				pool += freq[i] - t
			}
		}
		deficit := 0
		for i := 0; i < 26; i++ {
			if freq[i] < t {
				deficit += t - freq[i]
			}
		}
		if pool >= deficit {
			ops = pool // delete extras after converting deficit
		} else {
			ops = deficit // convert all pool + insert rest; deletions 0
			// convert pool + insert (deficit-pool) = deficit, plus delete 0
		}
		// When pool >= deficit: convert deficit + delete (pool-deficit) = pool
		if ops < ans {
			ans = ops
		}
		_ = dp0
		_ = dp1
	}
	// also target 0
	if len(s) < ans {
		ans = len(s)
	}
	return ans
}

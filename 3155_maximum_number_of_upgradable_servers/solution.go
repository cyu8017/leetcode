// LeetCode 3155 - Maximum Number of Upgradable Servers
// https://leetcode.com/problems/maximum-number-of-upgradable-servers/

func maxUpgrades(count []int, upgrade []int, sell []int, money []int) (ans []int) {
	for i, cnt := range count {
		ans = append(ans, min(cnt, (cnt*sell[i]+money[i])/(upgrade[i]+sell[i])))
	}
	return
}

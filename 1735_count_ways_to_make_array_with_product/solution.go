// LeetCode 1735 - Count Ways to Make Array With Product
// https://leetcode.com/problems/count-ways-to-make-array-with-product/

func waysToFillArray(queries [][]int) []int {
    const mod = 1000000007
    powMod := func(base, exp int) int {
        result := 1
        base %= mod
        for exp > 0 {
            if exp&1 == 1 {
                result = result * base % mod
            }
            base = base * base % mod
            exp >>= 1
        }
        return result
    }
    combMod := func(a, b int) int {
        num, den := 1, 1
        for i := 1; i <= b; i++ {
            num = num * ((a - b + i) % mod) % mod
            den = den * i % mod
        }
        return num * powMod(den, mod-2) % mod
    }
    ans := make([]int, 0, len(queries))
    for _, query := range queries {
        n, value := query[0], query[1]
        ways := 1
        d := 2
        for d*d <= value {
            if value%d == 0 {
                exp := 0
                for value%d == 0 {
                    value /= d
                    exp++
                }
                ways = ways * combMod(n+exp-1, exp) % mod
            }
            if d == 2 {
                d++
            } else {
                d += 2
            }
        }
        if value > 1 {
            ways = ways * (n % mod) % mod
        }
        ans = append(ans, ways)
    }
    return ans
}

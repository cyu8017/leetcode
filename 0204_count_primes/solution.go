// LeetCode 0204 - Count Primes
func countPrimes(n int) int { if n <= 2 { return 0 }; prime := make([]bool, n); for i := range prime { prime[i] = true }; prime[0], prime[1] = false, false; for p := 2; p*p < n; p++ { if prime[p] { for m := p*p; m < n; m += p { prime[m] = false } } }; count := 0; for _, value := range prime { if value { count++ } }; return count }

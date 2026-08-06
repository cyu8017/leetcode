// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

impl Solution {
    pub fn ways_to_build_rooms(prev_room: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = prev_room.len();
        let mut children = vec![Vec::new(); n];
        for (room, &prev) in prev_room.iter().enumerate() {
            if prev != -1 {
                children[prev as usize].push(room);
            }
        }

        let mut fact = vec![1i64; n + 1];
        let mut inv_fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
            let mut result = 1i64;
            base %= modulus;
            while exp > 0 {
                if exp & 1 == 1 {
                    result = result * base % modulus;
                }
                base = base * base % modulus;
                exp >>= 1;
            }
            result
        }
        inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }

        fn comb(fact: &[i64], inv_fact: &[i64], a: usize, b: usize) -> i64 {
            fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD
        }

        fn dfs(
            node: usize,
            children: &[Vec<usize>],
            fact: &[i64],
            inv_fact: &[i64],
        ) -> (usize, i64) {
            let mut size = 0usize;
            let mut ways = 1i64;
            for &child in &children[node] {
                let (child_size, child_ways) = dfs(child, children, fact, inv_fact);
                ways = ways * child_ways % MOD * comb(fact, inv_fact, size + child_size, child_size)
                    % MOD;
                size += child_size;
            }
            (size + 1, ways)
        }

        dfs(0, &children, &fact, &inv_fact).1 as i32
    }
}

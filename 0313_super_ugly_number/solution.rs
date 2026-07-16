// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

impl Solution {
    pub fn nth_super_ugly_number(n: i32, primes: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut ugly = vec![1];
        let mut pointers = vec![0; primes.len()];

        while ugly.len() < n {
            let next_values: Vec<i64> = pointers
                .iter()
                .enumerate()
                .map(|(index, &pointer)| ugly[pointer] as i64 * primes[index] as i64)
                .collect();
            let next_ugly = *next_values.iter().min().unwrap() as i32;
            ugly.push(next_ugly);
            for (index, &prime) in primes.iter().enumerate() {
                if next_ugly == ugly[pointers[index]] * prime {
                    pointers[index] += 1;
                }
            }
        }

        *ugly.last().unwrap()
    }
}

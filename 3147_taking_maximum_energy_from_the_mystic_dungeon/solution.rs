// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

impl Solution {
    pub fn maximum_energy(energy: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let n = energy.len();
        let mut ans = -(1 << 30);
        for i in n - k..n {
            let mut s = 0;
            let mut j = i as i32;
            while j >= 0 {
                s += energy[j as usize];
                ans = ans.max(s);
                j -= k as i32;
            }
        }
        ans
    }
}

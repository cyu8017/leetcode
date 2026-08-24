// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

impl Solution {
    pub fn odd_even_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut next_higher = vec![0; n];
        let mut next_lower = vec![0; n];
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by(|&i, &j| arr[i].cmp(&arr[j]).then(i.cmp(&j)));
        let mut stack = Vec::new();
        for i in order {
            while !stack.is_empty() && *stack.last().unwrap() < i {
                next_higher[stack.pop().unwrap()] = i;
            }
            stack.push(i);
        }
        stack.clear();
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by(|&i, &j| arr[j].cmp(&arr[i]).then(i.cmp(&j)));
        for i in order {
            while !stack.is_empty() && *stack.last().unwrap() < i {
                next_lower[stack.pop().unwrap()] = i;
            }
            stack.push(i);
        }
        let mut odd = vec![false; n];
        let mut even = vec![false; n];
        odd[n - 1] = true;
        even[n - 1] = true;
        for i in (0..n - 1).rev() {
            if next_higher[i] != 0 {
                odd[i] = even[next_higher[i]];
            }
            if next_lower[i] != 0 {
                even[i] = odd[next_lower[i]];
            }
        }
        odd.iter().filter(|&&x| x).count() as i32
    }
}

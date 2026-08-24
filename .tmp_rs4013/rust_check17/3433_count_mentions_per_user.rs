struct Solution;
// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

impl Solution {
    pub fn count_mentions(number_of_users: i32, mut events: Vec<Vec<String>>) -> Vec<i32> {
        events.sort_by(|a, b| {
            let ti: i32 = a[1].parse().unwrap();
            let tj: i32 = b[1].parse().unwrap();
            if ti != tj {
                ti.cmp(&tj)
            } else {
                b[0].cmp(&a[0])
            }
        });
        let n = number_of_users as usize;
        let mut online = vec![true; n];
        let mut offline_until = vec![0; n];
        let mut ans = vec![0; n];
        for e in events {
            let t: i32 = e[1].parse().unwrap();
            for i in 0..n {
                if !online[i] && offline_until[i] <= t {
                    online[i] = true;
                }
            }
            if e[0] == "OFFLINE" {
                let id: usize = e[2].parse().unwrap();
                online[id] = false;
                offline_until[id] = t + 60;
            } else {
                let msg = &e[2];
                if msg == "ALL" {
                    for i in 0..n {
                        ans[i] += 1;
                    }
                } else if msg == "HERE" {
                    for i in 0..n {
                        if online[i] {
                            ans[i] += 1;
                        }
                    }
                } else {
                    for part in msg.split_whitespace() {
                        let id: usize = part[2..].parse().unwrap();
                        ans[id] += 1;
                    }
                }
            }
        }
        ans
    }
}

fn main() {}

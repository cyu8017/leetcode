// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

impl Solution {
    pub fn friend_requests(
        n: i32,
        restrictions: Vec<Vec<i32>>,
        requests: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        let mut ans = vec![false; requests.len()];
        for (i, req) in requests.iter().enumerate() {
            let u = find(&mut parent, req[0] as usize);
            let v = find(&mut parent, req[1] as usize);
            let mut ok = true;
            if u != v {
                for r in &restrictions {
                    let x = find(&mut parent, r[0] as usize);
                    let y = find(&mut parent, r[1] as usize);
                    if (x == u && y == v) || (x == v && y == u) {
                        ok = false;
                        break;
                    }
                }
            }
            ans[i] = ok;
            if ok {
                let a = find(&mut parent, u);
                let b = find(&mut parent, v);
                if a != b {
                    parent[a] = b;
                }
            }
        }
        ans
    }
}

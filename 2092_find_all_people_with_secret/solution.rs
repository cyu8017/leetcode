// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let n = n as usize;
        let mut meetings = meetings;
        meetings.sort_by_key(|m| m[2]);
        let mut parent: Vec<usize> = (0..n).collect();
        fn find(parent: &mut [usize], x: usize) -> usize {
            if parent[x] != x {
                parent[x] = find(parent, parent[x]);
            }
            parent[x]
        }
        fn unite(parent: &mut [usize], a: usize, b: usize) {
            let a = find(parent, a);
            let b = find(parent, b);
            if a != b {
                parent[a] = b;
            }
        }
        let mut know = vec![false; n];
        know[0] = true;
        know[first_person as usize] = true;
        unite(&mut parent, 0, first_person as usize);
        let mut i = 0;
        while i < meetings.len() {
            let t = meetings[i][2];
            let mut j = i;
            while j < meetings.len() && meetings[j][2] == t {
                j += 1;
            }
            for k in i..j {
                unite(&mut parent, meetings[k][0] as usize, meetings[k][1] as usize);
            }
            let root0 = find(&mut parent, 0);
            let mut reset = Vec::new();
            for k in i..j {
                let a = meetings[k][0] as usize;
                let b = meetings[k][1] as usize;
                if find(&mut parent, a) != root0 {
                    reset.push(a);
                    reset.push(b);
                } else {
                    know[a] = true;
                    know[b] = true;
                }
            }
            for x in reset {
                parent[x] = x;
            }
            i = j;
        }
        (0..n)
            .filter(|&i| find(&mut parent, i) == find(&mut parent, 0) || know[i])
            .map(|i| i as i32)
            .collect()
    }
}

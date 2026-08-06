// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

pub struct LockingTree {
    locked: Vec<i32>,
    parent: Vec<i32>,
    children: Vec<Vec<usize>>,
}

impl LockingTree {
    pub fn new(parent: Vec<i32>) -> Self {
        let n = parent.len();
        let mut children = vec![Vec::new(); n];
        for (son, &fa) in parent.iter().enumerate().skip(1) {
            children[fa as usize].push(son);
        }
        Self {
            locked: vec![-1; n],
            parent,
            children,
        }
    }

    pub fn lock(&mut self, num: i32, user: i32) -> bool {
        let num = num as usize;
        if self.locked[num] == -1 {
            self.locked[num] = user;
            true
        } else {
            false
        }
    }

    pub fn unlock(&mut self, num: i32, user: i32) -> bool {
        let num = num as usize;
        if self.locked[num] == user {
            self.locked[num] = -1;
            true
        } else {
            false
        }
    }

    pub fn upgrade(&mut self, num: i32, user: i32) -> bool {
        let num = num as usize;
        let mut x = num as i32;
        while x != -1 {
            if self.locked[x as usize] != -1 {
                return false;
            }
            x = self.parent[x as usize];
        }

        let mut find = false;
        Self::dfs(&self.children, &mut self.locked, num, &mut find);
        if !find {
            return false;
        }
        self.locked[num] = user;
        true
    }

    fn dfs(children: &[Vec<usize>], locked: &mut [i32], u: usize, find: &mut bool) {
        for &v in &children[u] {
            if locked[v] != -1 {
                locked[v] = -1;
                *find = true;
            }
            Self::dfs(children, locked, v, find);
        }
    }
}

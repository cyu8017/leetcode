// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq)]
pub struct Node {
    pub val: i32,
    pub children: Vec<Rc<RefCell<Node>>>,
}

impl Solution {
    pub fn move_sub_tree(
        root: Option<Rc<RefCell<Node>>>,
        p: Option<Rc<RefCell<Node>>>,
        q: Option<Rc<RefCell<Node>>>,
    ) -> Option<Rc<RefCell<Node>>> {
        let root = root?;
        let p = p?;
        let q = q?;
        let mut parent: HashMap<*const RefCell<Node>, Rc<RefCell<Node>>> = HashMap::new();

        fn build(
            node: &Rc<RefCell<Node>>,
            parent: &mut HashMap<*const RefCell<Node>, Rc<RefCell<Node>>>,
        ) {
            let children = node.borrow().children.clone();
            for child in children {
                parent.insert(Rc::as_ptr(&child), node.clone());
                build(&child, parent);
            }
        }
        build(&root, &mut parent);

        if parent
            .get(&Rc::as_ptr(&p))
            .map_or(false, |par| Rc::ptr_eq(par, &q))
        {
            return Some(root);
        }

        let is_ancestor = |a: &Rc<RefCell<Node>>, b: &Rc<RefCell<Node>>| -> bool {
            let mut cur = b.clone();
            loop {
                match parent.get(&Rc::as_ptr(&cur)) {
                    Some(par) if Rc::ptr_eq(par, a) => return true,
                    Some(par) => cur = par.clone(),
                    None => return false,
                }
            }
        };

        let remove_child = |par: &Rc<RefCell<Node>>, child: &Rc<RefCell<Node>>| {
            par.borrow_mut()
                .children
                .retain(|c| !Rc::ptr_eq(c, child));
        };

        let replace_child =
            |par: &Rc<RefCell<Node>>, old: &Rc<RefCell<Node>>, neu: &Rc<RefCell<Node>>| {
                let mut bor = par.borrow_mut();
                if let Some(i) = bor.children.iter().position(|c| Rc::ptr_eq(c, old)) {
                    bor.children[i] = neu.clone();
                }
            };

        let p_parent = parent.get(&Rc::as_ptr(&p)).cloned();
        let q_parent = parent.get(&Rc::as_ptr(&q)).cloned();
        let mut root = root;

        if is_ancestor(&p, &q) {
            if let Some(ref qp) = q_parent {
                remove_child(qp, &q);
            }
            if let Some(ref pp) = p_parent {
                replace_child(pp, &p, &q);
            } else {
                root = q.clone();
            }
            q.borrow_mut().children.push(p);
        } else {
            if let Some(ref pp) = p_parent {
                remove_child(pp, &p);
            } else {
                root = q.clone();
            }
            q.borrow_mut().children.push(p);
        }
        Some(root)
    }
}

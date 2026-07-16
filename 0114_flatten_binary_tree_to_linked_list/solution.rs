use std::cell::RefCell; use std::rc::Rc;
#[derive(Debug, PartialEq, Eq)] pub struct TreeNode { pub val:i32, pub left:Option<Rc<RefCell<TreeNode>>>, pub right:Option<Rc<RefCell<TreeNode>>> }
impl TreeNode { pub fn new(val:i32)->Self { Self { val,left:None,right:None } } }
impl Solution { pub fn flatten(root:&mut Option<Rc<RefCell<TreeNode>>>) {
    fn walk(n:Option<Rc<RefCell<TreeNode>>>, prev:&mut Option<Rc<RefCell<TreeNode>>>) {
        if let Some(n)=n { let (l,r)={let x=n.borrow();(x.left.clone(),x.right.clone())}; walk(r,prev); walk(l,prev);
            let mut x=n.borrow_mut(); x.right=prev.take(); x.left=None; *prev=Some(n.clone()); }
    } walk(root.clone(),&mut None);
} }
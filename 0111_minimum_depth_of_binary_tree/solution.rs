use std::cell::RefCell; use std::rc::Rc;
#[derive(Debug, PartialEq, Eq)] pub struct TreeNode { pub val:i32, pub left:Option<Rc<RefCell<TreeNode>>>, pub right:Option<Rc<RefCell<TreeNode>>> }
impl TreeNode { pub fn new(val:i32)->Self { Self { val,left:None,right:None } } }
impl Solution { pub fn min_depth(root:Option<Rc<RefCell<TreeNode>>>) -> i32 {
    match root { None=>0, Some(n)=>{ let n=n.borrow(); match (&n.left,&n.right) {
        (None,None)=>1, (None,r)=>1+Self::min_depth(r.clone()), (l,None)=>1+Self::min_depth(l.clone()),
        (l,r)=>1+Self::min_depth(l.clone()).min(Self::min_depth(r.clone())) } } }
} }
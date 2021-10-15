package org.maslov.graph.sametree;


// leetcode same tree
public class SameTree {
    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) {
            return true;
        } else if (p == null && q != null) {
            return false;
        } else if (p !=null && q == null) {
            return false;
        } else {
            if (p.val != q.val) {
                return false;
            } else {
                int pcode = (p.left != null ? 1 << 1 : 0) | (p.right != null ? 1 : 0);
                int qcode = (q.left != null ? 1 << 1 : 0) | (q.right != null ? 1 : 0);
                if (pcode != qcode) {
                    return false;
                } else {
                    boolean left = true;
                    boolean right = true;
                    if (p.left != null) {
                        left = isSameTree(p.left, q.left);
                    }
                    if (p.right != null) {
                        right = isSameTree(p.right, q.right);
                    }
                    return left && right;
                }
            }
        }
    }

}
